from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import connection
from .serializers import ProfileSerializer


class ProfileView(APIView):
    permission_classes=[IsAuthenticated]


    def get (self,request):
        user=request.user
        acc=user.account_type

        with connection.cursor() as cursor :
            if acc == 'USER':
                cursor.execute('select * from user_info where u_username=%s',[user.username])
            if acc=='BENEFICIARY':
                cursor.execute('SELECT * FROM beneficiary where b_username=%s',[user.username])
            if acc=='GUARDIAN':
                cursor.execute('SELECT * FROM guardian_info WHERE g_username=%s',[user.username])
            row=cursor.fetchone()
        return Response({'data':row})
    def put(self,request):
        user=request.user
        acc=user.account_Type
        serializer=ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        with connection.cursor() as cursor:
            if acc=='USER':
                cursor.execute('''update user_info set
                                        u_full_name=coalesce(%s,u_full_name),
                                        u_phone_num=coalesce(%s,u_phone_num),
                                        u_gender = COALESCE(%s, u_gender), 
                                        u_dob = COALESCE(%s, u_dob),
                                        u_family_title = COALESCE(%s, u_family_title),
                                        fl_address = COALESCE(%s, fl_address),
                                        u_bio = COALESCE(%s, u_bio) 
                                        where u_username=%s
                               ''',
                                   [data.get['full_name'],
                                    data.get('phone_num'),
                                    data.get('gender'),
                                    data.get("dob"),
                                    data.get("family_title"),
                                    data.get("address"),
                                    data.get("bio"),
                                    user.username
                                    ]                 )
            elif acc='BENEFICIARY':
                cursor.execute('''UPDATE beneficiary 
                               SET 
                        b_full_name = COALESCE(%s, b_full_name),
                        b_phone_num = COALESCE(%s, b_phone_num),
                        b_gender = COALESCE(%s, b_gender),
                        b_dob = COALESCE(%s, b_dob),
                        b_family_title = COALESCE(%s, b_family_title)
                         WHERE b_username = %s
                               ''',[
                    data.get("full_name"),
                    data.get("phone"),
                    data.get("gender"),
                    data.get("dob"),
                    data.get("family_title"),
                    user.username]
    ) 
            elif acc=='GUARDIAN ':
                cursor.execute("""
                    UPDATE guardian_info
                    SET 
                        g_full_name = COALESCE(%s, g_full_name),
                        g_phone_num = COALESCE(%s, g_phone_num),
                        g_gender = COALESCE(%s, g_gender),
                        g_address = COALESCE(%s, g_address),
                        bio = COALESCE(%s, bio)
                    WHERE g_username = %s
                """, [
                    data.get("full_name"),
                    data.get("phone"),
                    data.get("gender"),
                    data.get("address"),
                    data.get("bio"),
                    user.username])
        return Response({'message':'Profile Updated Successfully'})