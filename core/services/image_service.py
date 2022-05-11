from core.models.image import Image, ItemImages


class ImageService:
    ALLOWED_EXTENSIONS = ("JPG", "jpg", "JPEG", "png", "PNG", "jpeg")

    @classmethod
    def create_image(cls, images, item):
        item_images = ItemImages(item=item)
        item_images.save()
        for idx, file in enumerate(images):
            file_name = "_".join([item.title, str(item.id), str(idx)])
            ext = file.name.split(".")[-1]
            if ext not in cls.ALLOWED_EXTENSIONS:
                break
            file.name = f"{file_name}.{ext}"
            temp = Image(name=file_name, image=file)
            temp.save()
            item_images.images.add(temp)
        item_images.save()

    @classmethod
    def get_images(cls, item):
        images = ItemImages.objects.filter(item=item)
        if len(images) == 0:
            # TODO: return default image
            default_image = Image.objects.filter(id=1)
            return default_image
        return images[0].images.all()

    @classmethod
    def update_profile_image(cls, user, image):
        file_name = "_".join([user.username])
        ext = image.name.split(".")[-1]
        if ext not in cls.ALLOWED_EXTENSIONS:
            return
        image.name = f"{file_name}.{ext}"
        temp = Image(name=file_name, image=image)
        temp.save()
        user.profile.image = temp
        user.save()
