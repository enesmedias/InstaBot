# Bu kod, instagrapi modülünü kullanarak Instagram'ın özel API'sine erişir
# ve takipçilerin isimlerini ekrana yeşil renkte ve > işaretiyle yazdırır.

# instagrapi modülünü içe aktar
from instagrapi import Client

# renk kodlarını tanımla
GREEN = "\033[92m"
YELLOW = "\033[93m"

def login(username, password):
    # Bu fonksiyon, verilen kullanıcı adı ve şifre ile Instagram'a giriş yapar
    # ve bir Client nesnesi döndürür.

    # Client sınıfından bir nesne oluştur
    client = Client()

    try:
        # Instagram'a giriş yap
        client.login(username, password)
        return client # Client nesnesini döndür
    except Exception as e:
        # Hata oluşursa, hata mesajını ekrana yazdır ve programdan çık
        print(f"Giriş yaparken bir hata oluştu: {e}")
        exit()

def get_user_id(client, username):
    # Bu fonksiyon, verilen kullanıcı adının ID'sini alır ve döndürür.

    try:
        # kullanıcının ID'sini al
        user_id = client.user_id_from_username(username)
        return user_id # ID'yi döndür
    except Exception as e:
        # Hata oluşursa, hata mesajını ekrana yazdır ve programdan çık
        print(f"Kullanıcı ID'si alınırken bir hata oluştu: {e}")
        exit()

def get_followers_ids(client, user_id):
    # Bu fonksiyon, verilen kullanıcının takipçilerinin ID'lerini alır ve döndürür.

    try:
        # kullanıcının takipçilerinin ID'lerini al
        followers_ids = client.user_followers(user_id)
        return followers_ids # ID'leri döndür
    except Exception as e:
        # Hata oluşursa, hata mesajını ekrana yazdır ve programdan çık
        print(f"Takipçilerin ID'leri alınırken bir hata oluştu: {e}")
        exit()

def get_follower_name(client, follower_id):
    # Bu fonksiyon, verilen takipçinin ismini alır ve döndürür.

    try:
        # takipçinin ismini al
        follower_name = client.user_info(follower_id).username
        return follower_name # ismi döndür
    except Exception as e:
        # Hata oluşursa, hata mesajını ekrana yazdır ve programdan çık
        print(f"Takipçinin ismi alınırken bir hata oluştu: {e}")
        exit()

def input_username():
    # Bu fonksiyon, kullanıcıdan bir Instagram kullanıcı adı ister ve döndürür.

    while True: # sonsuz döngü başlat
        # input fonksiyonu ile kullanıcı adı al
        username = input("Instagram kullanıcı adını girin: ")

        # kullanıcı adının boş olmadığını kontrol et
        if username.strip():
            return username # kullanıcı adını döndür
        else:
            print("Lütfen geçerli bir kullanıcı adı girin.") # uyarı mesajı ver

def main():
    # Ana fonksiyon

    # sarı renkte hesap şifreniz ve kullanıcı adınızı isteyen input fonksiyonları ile kendi hesabınızın kullanıcı adı ve şifresini al
    print(YELLOW + "Sizin hesabınızın kullanıcı adını girin: ", end="")
    my_username = input()
    print(YELLOW + "Sizin hesabınızın şifresini girin: ", end="")
    my_password = input()

    # Instagram'a giriş yap ve bir Client nesnesi al
    client = login(my_username, my_password)

    # input fonksiyonu ile takipçilerini almak istediğiniz kullanıcı adını al
    username = input_username()

    # kullanıcının ID'sini al
    user_id = get_user_id(client, username)

    # kullanıcının takipçilerinin ID'lerini al
    followers_ids = get_followers_ids(client, user_id)

    # takipçilerin sayısını ekrana yazdır
    print(f"{username} kullanıcısının {len(followers_ids)} takipçisi var.")

    # takipçilerin ID'lerinden isimlerini al ve ekrana yeşil renkte ve > işaretiyle yazdır
    for follower_id in followers_ids:
        follower_name = get_follower_name(client, follower_id) # takipçinin ismini al
        print(GREEN, follower_name, sep="> ") # yeşil renkte ve > işaretiyle yazdır

# Ana fonksiyonu çağır
main()
