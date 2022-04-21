from django.contrib import admin
from .models import User, Book, BookUser, CommentUser,Comment

# Register your models here.
admin.site.register([User,Book,BookUser,Comment,CommentUser])