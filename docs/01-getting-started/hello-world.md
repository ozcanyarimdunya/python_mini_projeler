# Hello World

Pythonda diğer programlama dillerine nazaren daha az syntax kullanılır
Örneğin C de yazacağınız bir hello world uygulaması için;

```c
# include<stdio.h>
# include<stdlib.h>

int main()
{
    printf("Hello World");
    system("pause");
    return 0;
}
```


kodlarını yazmanız gerekmektedir.
Çok fazla kod satırı ve syntax özellikle büyük programlarda çok karmaşık olur
Derlenmesi, çalıştırılması buna bağlı olarak zaman almakta ve performans kaybı yaşatmaktadır

Gelin pythonda basit bir hello world uygulaması nasıl yazılır ona bakalım

```python
print("Hello World")
```

Ve uygulamamız tamamdır.
Sadece tek satırlık bir kod, C de bu 8 satır yer kaplamıştı
Üstelik platform bağımsız çalışacak bir uygulama oldu

Output için extra bir dosya oluşturmadan .py dosyamızı istediğimiz işletim
sisteminde kullanabiliriz artık
İşletim sisteminde Python kurulu olması lazım

Linux tabanlı çoğu işletim sisteminde python default olarak kurulu gelmektedir
Yalnız windows ta kendiniz kurmanız lazım boyutu çok büyük değil max 50MB dır

**Output:**
```text
Hello World

Process finished with exit code 0
```
