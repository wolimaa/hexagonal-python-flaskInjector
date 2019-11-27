from interface import implements, Interface


class IAsoService(Interface):
    def get(self, oid):
        pass

    def update(self, oid, aso):
        pass
