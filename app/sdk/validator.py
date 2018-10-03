from sdk.filter import NumberFilter


class NumberValidate:
    @staticmethod
    def integer(value, label=''):
        value = NumberFilter.integer(value)
        if value is None:
            return True

        if not isinstance(value, int):
            raise Exception('{} debe ser un número entero'.format(label).strip())
        return True
