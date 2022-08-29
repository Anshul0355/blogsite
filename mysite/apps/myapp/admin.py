from django.contrib import admin
from .models import Post,Comment
from django.utils.html import format_html
# from django.contrib.auth.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	model = Post

	list_display = ['id','title','is_good', 'button']
	actions=['make_good', 'make_bad']

	def make_good(self,request,queryset):
		queryset.update(is_good = True)

	def make_bad(self,request,queryset):
		queryset.update(is_good = False)

	def button(self,request):
		pk = request.id
		# import pdb;pdb.set_trace()	
		post=self.model.objects.get(id=pk)
		post.is_good=True
		post.save()
		return format_html(
			'<input type="button" id="%s" value="make_good">'% (pk)
			# '<buttton id ="%s">make good</button>' % (post.id)
			)


	# def button2(self,request):
	# 	# import pdb;pdb.set_trace()
	# 	pk = request.id
	# 	post=self.model.objects.get(id=pk)
	# 	post.is_good=False
	# 	post.save()
	# 	# self.model.objects.update(is_good=True)
	# 	return format_html(
	# 		'<button  > Make bad</button>'
	# 		)

# admin.site.register(Post)
admin.site.register(Comment)

