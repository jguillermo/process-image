from sdk.filter import Filter



class Process:
    @staticmethod
    def integer(value, label=''):

        value = Filter.integer(value)

        if value is None:
            raise Exception('{} es requerido'.format(label).strip())

        if not isinstance(value, int):
            raise Exception('{} debe ser un número entero'.format(label).strip())

        return value

    @staticmethod
    def string(value, label=''):

        value = Filter.integer(value)

        if value is None:
            raise Exception('{} es requerido'.format(label).strip())

        if not isinstance(value, str):
            raise Exception('{} debe ser un string'.format(label).strip())

        return value
