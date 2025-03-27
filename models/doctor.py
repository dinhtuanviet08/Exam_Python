class Doctor:
    def __init__(self, full_name, specialization, phone, email, experience):
        self.full_name = full_name
        self.specialization = specialization
        self.phone = phone
        self.email = email
        self.experience = experience

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "specialization": self.specialization,
            "phone": self.phone,
            "email": self.email,
            "experience": self.experience
        }
