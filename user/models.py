
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
# Create your models here.

class Customuser(AbstractUser):
    profile_photo = models.CharField(max_length=400,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(null=True,blank=True,max_length=30)
    SecureCode = models.CharField(max_length=30,blank=True)

    REQUIRED_FIELDS = ['profile_photo','address','city','phone_number']

import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.
import random
class QrCode(models.Model):
   user = models.OneToOneField(Customuser,on_delete=models.CASCADE)
   image=models.ImageField(upload_to='qrcode',blank=True)


   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make("{} - {}".format(self.user.username,self.user.SecureCode))
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)




from allauth.account.signals import user_signed_up, user_logged_in
import hashlib
@receiver(user_signed_up)
def social_login_fname_lname_profilepic(request, user, sociallogin=None, **kwargs):
    preferred_avatar_size_pixels=256

    picture_url = "http://www.gravatar.com/avatar/{0}?s={1}".format(
        hashlib.md5(user.email.encode('UTF-8')).hexdigest(),
        preferred_avatar_size_pixels
    )

    print("Test")
    if sociallogin:
        print("Test")
        print(sociallogin.account.extra_data)
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'twitter':
            name = sociallogin.account.extra_data['name']
            user.first_name = name.split()[0]
            user.last_name = name.split()[1]

        if sociallogin.account.provider == 'facebook':
            print("Facebookj")

            f_name = sociallogin.account.extra_data['first_name']
            l_name = sociallogin.account.extra_data['last_name']
            if f_name:
                user.first_name = f_name
            if l_name:
                user.last_name = l_name

            #verified = sociallogin.account.extra_data['verified']
            picture_url =  sociallogin.account.extra_data['picture']['data']['url']
            print(picture_url)
            user.profile_photo = picture_url

    user.save()
 