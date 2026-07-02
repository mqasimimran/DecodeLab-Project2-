from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, default="user")
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        # The Neurotransmitter: Formatting data as lightweight JSON
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }