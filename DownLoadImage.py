import requests

pic_url='https://pixabay.com/en/arcades-arcade-architecture-city-3428490/'
with open('pic1.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
