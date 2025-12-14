from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import connection
from .serializers import ProfileSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # ❌ REMOVE: account_type / multiple table logic
        # acc = user.account_type

        # ✅ ADD: single profile fetch
        data = self.fetch_profile(user.id)

        return Response(data)

    def fetch_profile(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    full_name,
                    phone_num,
                    gender,
                    dob,
                    family_title,
                    address,
                    bio,
                    nationality,
                    region,
                    relation_to_user
                FROM user_profile
                WHERE user_id = %s
                """,
                [user_id]
            )
            row = cursor.fetchone()

        return row

    def put(self, request):
        user = request.user

        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE user_profile
                SET
                    full_name = COALESCE(%s, full_name),
                    phone_num = COALESCE(%s, phone_num),
                    gender = COALESCE(%s, gender),
                    dob = COALESCE(%s, dob),
                    family_title = COALESCE(%s, family_title),
                    address = COALESCE(%s, address),
                    bio = COALESCE(%s, bio),
                    nationality = COALESCE(%s, nationality),
                    region = COALESCE(%s, region),
                    relation_to_user = COALESCE(%s, relation_to_user)
                WHERE user_id = %s
                """,
                [
                    data.get("full_name"),
                    data.get("phone_num"),
                    data.get("gender"),
                    data.get("dob"),
                    data.get("family_title"),
                    data.get("address"),
                    data.get("bio"),
                    data.get("nationality"),
                    data.get("region"),
                    data.get("relation_to_user"),
                    user.id,
                ],
            )

        return Response({"message": "Profile Updated Successfully"})
