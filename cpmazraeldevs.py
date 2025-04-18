import requests
import json
from concurrent.futures import ThreadPoolExecutor

__ENDPOINT_URL__: str = "https://cpmazraeldevs.squareweb.app/api/"

class cpmazraeldevs:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")  
    
    def delete(self):
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        params = {"key": self.access_key}
        response = requests.get(f"{__ENDPOINT_URL__}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = {"account_auth": self.auth_token, "name": name}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = {"account_auth": self.auth_token, "id": id}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_player_car(self, car_id) -> any:
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/delete_friends", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_w16", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_horns", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/disable_damage", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlimited_fuel", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_wins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_loses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_smoke(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_paid_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_paid_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_all_cars_siren(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars_siren", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def account_clone(self, account_email, account_password) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_plates(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_wheels(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_wheels", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_male(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def hack_car_speed(self, car_id, new_hp, new_inner_hp, new_nm, new_torque):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "new_hp": new_hp,
            "new_inner_hp": new_inner_hp,
            "new_nm": new_nm,
            "new_torque": new_torque,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/hack_car_speed", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def unlock_animations(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_animations", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def max_max1(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max1", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def max_max2(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/max_max2", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")  

    def Shiftime(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Shiftime", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")    
        
    def millage_car(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/millage_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def brake_car(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/brake_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_crown(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_crown", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def change_password(self, new_password):
        payload = {
            "account_auth": self.auth_token,
            "new_password": new_password
        }
        params = {"key": self.access_key}
    
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/change_password",
                params=params,
                data=payload,
                timeout=10
            )
            response_decoded = response.json()
            
            if response_decoded.get("new_token"):
                self.auth_token = response_decoded["new_token"]
                
            return response_decoded.get("ok", False)
            
        except requests.exceptions.RequestException:
            return False    

    def modificar_todos_los_autos(self, new_hp, new_inner_hp, new_nm, new_torque) -> bool:
        with open('car_ids.json', 'r') as file:
            car_ids = json.load(file)
        
        def modificar_auto(car_id):
            payload = {
                "account_auth": self.auth_token,
                "car_id": car_id,
                "new_hp": new_hp,
                "new_inner_hp": new_inner_hp,
                "new_nm": new_nm,
                "new_torque": new_torque,
            }
            params = {"key": self.access_key}
            try:
                response = requests.post(f"{__ENDPOINT_URL__}/hack_car_speed", 
                                      params=params, 
                                      data=payload,
                                      timeout=3)
                return response.json().get("ok", False)
            except:
                return False
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            list(executor.map(modificar_auto, car_ids))
        
        return True

    def Dez(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Dez", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")  

    def Rec(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Rec", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")  

    def Rig(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Rig", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def Inc(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Inc", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")    

    def Vid(self, car_id, custom):
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "custom": custom,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/Vid", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def change_email(self, new_email):
        """
        Cambia el correo electrónico asociado a la cuenta
        
        Args:
            new_email (str): Nuevo correo electrónico a establecer
        
        Returns:
            bool: True si el cambio fue exitoso, False en caso contrario
        """
        payload = {
            "account_auth": self.auth_token,
            "new_email": new_email
        }
        params = {"key": self.access_key}
        
        try:
            response = requests.post(
                f"{__ENDPOINT_URL__}/change_email",
                params=params,
                data=payload,
                timeout=10
            )
            response_decoded = response.json()
            
            # Actualizar el token si viene en la respuesta
            if response_decoded.get("new_token"):
                self.auth_token = response_decoded["new_token"]
                
            return response_decoded.get("ok", False)
            
        except requests.exceptions.RequestException:
            return False 
            
    def front_bumper(self, car_id) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/front_bumper", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok", False)

    def rear_bumper(self, car_id) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/rear_bumper", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok", False)

    def clone_car_design(self, source_car_id, target_car_id) -> bool:
        payload = {
        "account_auth": self.auth_token,
        "source_car_id": source_car_id,
        "target_car_id": target_car_id
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/clone_car_design", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok", False)

    def clone_plates_only(self, account_email, account_password) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "to_email": account_email,
            "to_password": account_password
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/clone_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def apply_chrome_parts(self, car_id, color_number):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "color_number": color_number
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/apply_chrome_parts", params=params, data=payload)
        return response.json()

    def apply_chrome_parts(self, car_id, color_number):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "color_number": color_number
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/apply_chrome_parts", params=params, data=payload)
        return response.json()

    def apply_paint_only(self, car_id: int):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/apply_paint_only", params=params, data=payload)
        return response.json()
    
