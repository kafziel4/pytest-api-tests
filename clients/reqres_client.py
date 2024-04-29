import requests


class ReqResClient:
    __base_url = "https://reqres.in/api"
    __users_path = "users"
    __colors_path = "colors"
    __register_path = "register"
    __login_path = "login"

    def get_users(self, page):
        return requests.get(f"{self.__base_url}/{self.__users_path}", params={"page": page})

    def get_single_user(self, user_id):
        return requests.get(f"{self.__base_url}/{self.__users_path}/{user_id}")

    def post_user(self, body):
        return requests.post(f"{self.__base_url}/{self.__users_path}", json=body)

    def put_user(self, user_id, body):
        return requests.put(f"{self.__base_url}/{self.__users_path}/{user_id}", json=body)

    def patch_user(self, user_id, body):
        return requests.patch(f"{self.__base_url}/{self.__users_path}/{user_id}", json=body)

    def delete_user(self, user_id):
        return requests.delete(f"{self.__base_url}/{self.__users_path}/{user_id}")

    def get_colors(self):
        return requests.get(f"{self.__base_url}/{self.__colors_path}")

    def get_single_color(self, color_id):
        return requests.get(f"{self.__base_url}/{self.__colors_path}/{color_id}")

    def post_register(self, body):
        return requests.post(f"{self.__base_url}/{self.__register_path}", json=body)

    def post_login(self, body):
        return requests.post(f"{self.__base_url}/{self.__login_path}", json=body)
