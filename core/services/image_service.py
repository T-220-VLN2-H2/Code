from core.models.image import Image, ItemImages


class ImageService:
    @staticmethod
    def create_image(images, item):
        item_images = ItemImages(item=item)
        item_images.save()
        for idx, file in enumerate(images):
            file_name = "_".join([item.title, str(item.id), str(idx)])
            ext = file.name.split(".")[-1]
            if ext not in ("JPG", "jpg", "JPEG", "png", "PNG", "jpeg"):
                break
            file.name = f"{file_name}.{ext}"
            temp = Image(name=file_name, image=file)
            temp.save()
            item_images.images.add(temp)
        item_images.save()

    @staticmethod
    def get_images(item):
        images = ItemImages.objects.filter(item=item)
        if len(images) == 0:
            # TODO: return default image
            default_image = Image.objects.filter(id=9)
            return default_image
        return images[0].images.all()
