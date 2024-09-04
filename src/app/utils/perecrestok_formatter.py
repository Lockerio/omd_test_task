from typing import Any


class PerecrestokFormatter:
    @staticmethod
    def src_json_to_output_json(src_data: dict[str, Any]) -> dict[str, Any]:
        src_data = src_data["content"]
        if src_data["priceTag"]["grossPrice"]:
            price = src_data["priceTag"]["price"] / 100
            gross_price = src_data["priceTag"]["grossPrice"] / 100
        else:
            price = None
            gross_price = src_data["priceTag"]["price"] / 100

        images = [
            {
                "image_url": image["cropUrlTemplate"]
            }
            for image in src_data["images"]
        ]

        brand = None
        try:
            for element in src_data["analyticsInfo"]:
                if element["name"] == "brandName":
                    brand = element["value"]
        except:
            pass

        content_url = (f'https://www.perekrestok.ru/cat/{src_data["catalogPrimaryCategory"]["id"]}/p/'
                       f'{src_data["masterData"]["slug"]}-{src_data["plu"]}')

        data = {
            "name": src_data["title"],
            "price": gross_price,
            "price_sale": price,
            "description": src_data["description"],
            "code": src_data["plu"],
            "images": images,
            "comment_count": src_data["reviewCount"],
            "rating": src_data["rating"] / 100,
            "brand": brand,
            "categories": [
                src_data["catalogPrimaryCategory"]["title"],
                src_data["primaryCategory"]["title"]
            ],
            "content_url": content_url
        }

        return data

    @staticmethod
    def json_to_db_json(src_data: dict[str, Any]) -> dict[str, Any]:
        image_urls = ";".join([image["image_url"] for image in src_data["images"]])
        categories_str = ";".join(src_data["categories"])

        src_data["images"] = image_urls
        src_data["categories"] = categories_str

        return src_data
