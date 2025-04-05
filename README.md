# Kitap Yazma Rehberi

## PDF'e Derleme

- Eğer parça parça yapacak isen (kolay yönetilmesi için):

```bash
Get-Content -Path chapters/*.md -Encoding UTF8 | Out-File -FilePath kitap.md -Encoding UTF8
```

``` bash
pandoc kitap.md -o kitap.pdf --pdf-engine=xelatex
pandoc metadata.yml kitap.md -o kitap.pdf --pdf-engine=xelatex --toc # metadata ile
```

- Çıktı: kitap.pdf (Aynı klasörde oluşur)

---

``` bash
pandoc kitap.md -o kitap.html   # Web sayfası
pandoc kitap.md -o kitap.epub   # E-kitap
```

## Sorun Çözme

- Kitap Kapağı İşi: 1200x1800 30dpi 

- Derleme İşi

```json
"command": "powershell -Command \"jupyter nbconvert chapters/*.ipynb --to markdown; Get-Content chapters/*.md -Encoding UTF8 | Out-File kitap.md -Encoding UTF8; pandoc kitap.md -o kitap.pdf --pdf-engine=xelatex\"",
"command": "powershell -Command \"Get-Content chapters/*.md -Encoding UTF8 | Out-File kitap.md -Encoding UTF8; pandoc kitap.md -o kitap.pdf --pdf-engine=xelatex\"",
```


- LaTeX Hatası Alırsan

```bash
sudo tlmgr install cm-super amsmath  # MikTeX'te "Paket Yöneticisi"nden kurun
```

- Pandoc bulunamadı: PATH'e ekleyin veya terminali yeniden başlatın.

## Jupyter Bölümlerini Eklemek İçin

```bash
jupyter nbconvert --to markdown chapters/04-veri_analizi.ipynb
```
