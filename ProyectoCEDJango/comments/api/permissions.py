from rest_framework.permissions import BasePermission
from ..models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']  # argumento por teclado primary key
            comment = Comment.objects.get(pk=id_comment)
            id_user = request.user.pk
            user_id_comment = comment.user_id
            if id_user == user_id_comment:
                return True

            return False
