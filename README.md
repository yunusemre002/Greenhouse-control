## GREENHOUSE CONTROL SYSTEM

- Sistemde 3 adet sera ve 1 adet server bulunmaktadır. 
- Sistem kapalı çevrim bir networkten oluşmaktadır. 
- Bu kapalı sistemi, HAMACHİ yardımıyla gerçekleştirilmiştir. 
- Uygulamaya ait web ara yüzü açık kaynak kodlu bir yazılımdan temin edilmiştir. (Ek-1) 
- Mevcut ara yüzde 3 adet sera (sera1 sera2 ve sera3) bilgisi görülmektedir. 
- Bu seralara ait anlık sıcaklık değerleri Gauge chart’lar yardımıyla gösterilmiştir. 
- İstenilen sıcaklık değerleri ise ilgili seralara ait “istenilen sıcaklık gönderme kutucuğundan girilmekte ve ilgili seraya gönderilmektedir. 
- Arayüz HTML, CSS ve JavaScript ile oluşturulmuştur.  

- Sistem temelde 2 ana ayaktan oluşmaktadır. Bu ayaklar clientlar ve serverdır. Server kısmı Python Flask ile yazılmıştır. Server’ın ana görevi, Client ve ara yüz arasında ki iletişimi gerçekleştirmesidir. Yani seralardan gelen anlık sıcaklık bilgisini ara yüze aktarır ve ekranda görmemizi sağlar. Ekrandan girilen istenilen sıcaklık değerini de ilgili seraya gönderir. Client’ların görevi ise, serverdan aldığı istenilen sıcıcaklık bilgisini seraya iletmek ve seranın anık bilgisini servera iletmekten ibarettir.
- Ek-1: Ara yüzün temin edildiği adres [ https://codepen.io/bcarvalho/pen/oGGNea ]

- Proje tanıtım videosu linki : https://www.youtube.com/watch?v=TwIwN1CtNAw&ab_channel=YT%C3%9CElektrik-ElektronikFak%C3%BCltesi
