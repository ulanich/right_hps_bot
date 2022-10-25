class AlcoGame:
    members: dict = {}

    def reg_new_mem(self, message):
        self.members.update({message.from_user.username: message.from_user.id})

        pass
