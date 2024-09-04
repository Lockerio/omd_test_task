import requests


class PerecrestokParser:
    def __init__(self):
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "auth": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJqdGkiOiJkOWYwMDUwMS1iZWNiLTRiMmYtODcyZS1hMjMzZmE1YTIzNzkiLCJpYXQiOjE3MjU0NjQ5MDEsImV4cCI6MTcyNTQ5MzcwMSwiZCI6IjY1NzZlYThjLWFhYTktNDY5OS1iZjFhLTE5ZDA0YzYxZjljNSIsImFwaSI6IjEuNC4xLjAiLCJpcCI6IjM3LjEuMjAzLjcwIiwidSI6IjcwMDdhZGUzLWMzNWUtNDExMC04MjFiLTViNGZmNDY2MGM4MSIsInQiOjF9.AboBTZozdjsXf6kOhMSsFW0k22EkOEnu1f8QjQDdv_hyRNsyqumYck_ENOC7XWnj-500Rq_TtYPL2NaiyeZfu1PTAaHGicDnjcd4j5jGEYl3JojTCK-yoRAVa0JjZvw57ilzIs65IMcMOdAOMQrTF7mxYm7FSwjmcNrVpEwY2Sd--9TX",
            "cookie": "_gcl_au=1.1.1562277874.1725026467; _ga=GA1.1.795364619.1725026468; _ym_uid=1725026468214405476; _ym_d=1725026468; agreements=j:{\"isCookieAccepted\":true,\"isAdultContentEnabled\":false,\"isAppAppInstallPromptClosed\":false}; _ym_isad=1; httpsReferer=https%3A%2F%2Fwww.google.com%2F; TS015bfe9d=01b7bf3690d17b952032e9cd22dc47d3468b576ff2d764116632eb4263950d8b134c86ae22f5ce37f368035e85700bf51803fff590afbf1c42aca933bfdd5e26dda1d5436f3d5f04d002182797058ba62983d8efe4; session=j:{\"accessToken\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJqdGkiOiI3YjdiZjNmNC1lYWI2LTQ4ZjQtYTAxYS0yNjY3MTMxZTFkYzQiLCJpYXQiOjE3MjU0MzI5NTMsImV4cCI6MTcyNTQ2MTc1MywiZCI6IjY1NzZlYThjLWFhYTktNDY5OS1iZjFhLTE5ZDA0YzYxZjljNSIsImFwaSI6IjEuNC4xLjAiLCJpcCI6IjM3LjEuMjAzLjcwIiwidSI6IjcwMDdhZGUzLWMzNWUtNDExMC04MjFiLTViNGZmNDY2MGM4MSIsInQiOjF9.Abrq_lIK78Waccl5JN8DlKrhyo3_qGlXQP9Rnt9WlqHSG9cQfErMtOPcHS5B4HxRDbLVhc8VG8Ouj9S_FHD-b9a8AO8VsaOaWFnJaFEKJjGASul4J5q3CvxHcam5rUkNq8nukKu6LEc7OQpkWmmwE_DEM7qoKeLfTIM7Wola_BOI56yy\",\"refreshToken\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzUxMiJ9.eyJqdGkiOiJlOTQzZWI1NS04ZTlkLTRhMDQtODlhOC02NDc0OWFjOGM5ZWEiLCJpYXQiOjE3MjU0MzI5NTMsImV4cCI6MTc0MDk4NDk1MywiZCI6IjY1NzZlYThjLWFhYTktNDY5OS1iZjFhLTE5ZDA0YzYxZjljNSIsImFwaSI6IjEuNC4xLjAiLCJpcCI6IjM3LjEuMjAzLjcwIiwidSI6IjcwMDdhZGUzLWMzNWUtNDExMC04MjFiLTViNGZmNDY2MGM4MSIsInQiOjJ9.ADyBWHd4vZkEzipDaLblQe57Wfq2gz40cV_Dm20MHuXBAz3qPYaaAULQB6ZuGPFWzWAthipUGPJB6aSz-HtIrY1EARe3sDU8jAHZzzipzLPhHD96cf2vgPph_V78avEUqLdxEMCxTDa-eWUP5IfGU-6w7vbJyIwgklzWzH7X8PFruom1\",\"accessTokenExpiredAt\":1725461753610,\"refreshTokenExpiredAt\":1740984953610,\"device\":{\"uuid\":\"6576ea8c-aaa9-4699-bf1a-19d04c61f9c5\"}}; _ga_5K49P5RFR8=GS1.1.1725432953.2.1.1725434169.57.0.0",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Opera\";v=\"113\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0"
        }

    def get_product_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.json()
