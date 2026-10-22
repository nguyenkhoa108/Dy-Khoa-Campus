// Upload wave6 posts as scheduled posts. Usage in wp-admin page:
//   await (await fetch(RAW+'wave6/pub6.js')).text() -> eval; then pub6(RAW, ['slug1',...])
window.pub6 = async function (RAW, slugs) {
  const H = { 'X-WP-Nonce': wpApiSettings.nonce };
  const J = { ...H, 'Content-Type': 'application/json' };
  window.PUB6 = { st: 'run', done: [], err: [] };
  for (const slug of slugs) {
    try {
      const ex = await fetch('/blog/wp-json/wp/v2/posts?slug=' + slug + '&status=publish,future,draft,private&_fields=id', { headers: H }).then(r => r.json());
      if (ex.length) { PUB6.done.push({ slug, skip: ex[0].id }); continue; }
      const P = await fetch(RAW + 'wave6/' + slug + '.json').then(r => r.json());
      const svg = await fetch(RAW + 'wave6/' + slug + '.svg').then(r => r.text());
      const img = new Image(); img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg); await img.decode();
      const cv = new OffscreenCanvas(1200, 675); cv.getContext('2d').drawImage(img, 0, 0, 1200, 675);
      const blob = await cv.convertToBlob({ type: 'image/webp', quality: 0.85 });
      const fd = new FormData(); fd.append('file', new File([blob], slug + '.webp', { type: 'image/webp' }));
      const m = await fetch('/blog/wp-json/wp/v2/media', { method: 'POST', headers: H, body: fd }).then(r => r.json());
      if (!m.id) throw new Error('media ' + JSON.stringify(m).slice(0, 200));
      await fetch('/blog/wp-json/wp/v2/media/' + m.id, { method: 'POST', headers: J, body: JSON.stringify({ alt_text: P.cover_alt, title: P.title }) });
      const tags = [];
      for (const t of P.tags || []) {
        const r = await fetch('/blog/wp-json/wp/v2/tags?search=' + encodeURIComponent(t) + '&per_page=100', { headers: H }).then(r => r.json());
        let f = r.find(x => x.name.toLowerCase() === t.toLowerCase());
        if (!f) f = await fetch('/blog/wp-json/wp/v2/tags', { method: 'POST', headers: J, body: JSON.stringify({ name: t }) }).then(r => r.json());
        if (f.id) tags.push(f.id); else if (f.data && f.data.term_id) tags.push(f.data.term_id);
      }
      const body = {
        title: P.title, slug, content: P.content, excerpt: P.excerpt, status: 'future', date: P.publish_at,
        categories: P.categories, tags, featured_media: m.id,
        meta: { _yoast_wpseo_focuskw: P.focus_kw, _yoast_wpseo_title: P.seo_title, _yoast_wpseo_metadesc: P.meta_desc }
      };
      const p = await fetch('/blog/wp-json/wp/v2/posts', { method: 'POST', headers: J, body: JSON.stringify(body) }).then(r => r.json());
      if (!p.id) throw new Error('post ' + JSON.stringify(p).slice(0, 300));
      PUB6.done.push({ slug, id: p.id, status: p.status, date: p.date, media: m.id });
    } catch (e) { PUB6.err.push({ slug, e: String(e) }); }
  }
  PUB6.st = 'end';
};
'pub6 loaded';
