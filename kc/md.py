import json,re,html,sys
f=sys.argv[1]; out=sys.argv[2]; when=sys.argv[3]
d=json.load(open(f)); c=d['content']
c=re.sub(r'<h2[^>]*>(.*?)</h2>',r'\n## \1\n',c); c=re.sub(r'<h3[^>]*>(.*?)</h3>',r'\n### \1\n',c)
c=re.sub(r'<li>(.*?)</li>',r'- \1\n',c); c=re.sub(r'<strong>(.*?)</strong>',r'**\1**',c); c=re.sub(r'<em>(.*?)</em>',r'*\1*',c)
c=re.sub(r'<a href="([^"]+)">(.*?)</a>',r'[\2](\1)',c); c=re.sub(r'<summary>(.*?)</summary>',r'\n## \1\n',c)
c=re.sub(r'<hr[^>]*>','\n---\n',c); c=re.sub(r'<!--.*?-->','',c); c=re.sub(r'<[^>]+>','',c); c=html.unescape(c); c=re.sub(r'\n{3,}','\n\n',c)
head=f"# {d['title']}\n\n| Trường | Nội dung |\n|---|---|\n| Slug | {d['slug']} |\n| SEO title | {d['seo_title']} |\n| Meta ({len(d['meta_desc'])} ký tự) | {d['meta_desc']} |\n| Focus keyword | {d['focus_kw']} |\n| Chuyên mục | Truyền thông khoa học > Lý thuyết & Mô hình |\n| Tags | {', '.join(d['tags'])} |\n| Lịch đăng | {when} |\n\n---\n"
open(out,'w').write(head+c.strip()+'\n')
