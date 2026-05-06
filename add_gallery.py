f = open('index.html', 'r')
c = f.read()
f.close()
g = '<section id="galerie"><h2>Galerie</h2><div class="galerie-grid"><div class="galerie-item">Photo 1</div><div class="galerie-item">Photo 2</div><div class="galerie-item">Photo 3</div><div class="galerie-item">Photo 4</div><div class="galerie-item">Photo 5</div><div class="galerie-item">Photo 6</div></div></section>'

c = c.replace('<!-- FOOTER -->', g + '<!-- FOOTER -->')
f = open('index.html', 'w')
f.write(c)
f.close()
print('Done!')
0
