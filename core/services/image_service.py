from core.models import Image, Item


class ImageService:
    ALLOWED_EXTENSIONS = ("JPG", "jpg", "JPEG", "png", "PNG", "jpeg")

    @classmethod
    def create_image(cls, images, item: Item):
        for index, file in enumerate(images):

            file_name = "_".join([item.title, str(item.id), str(index)])
            ext = file.name.split(".")[-1]

            if ext not in cls.ALLOWED_EXTENSIONS:
                break

            file.name = f"{file_name}.{ext}"
            img = Image(name=file_name, image=file)
            img.save()
            item.images.add(img)
        item.save()

    @classmethod
    def get_images(cls, item):
        if item.images.count() == 0:
            default_image = Image.objects.get(id=385)
            return [default_image]

        return item.images.all()

    @classmethod
    def update_profile_image(cls, user, image):
        file_name = "_".join([user.username])
        ext = image.name.split(".")[-1]

        if ext not in cls.ALLOWED_EXTENSIONS:
            return

        image.name = f"{file_name}.{ext}"

        img = Image(name=file_name, image=image)
        img.save()

        user.profile.image = img
        user.save()
