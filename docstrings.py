"""Docstrings de uma linha simples."""

"""Docstrings de multiplas linhas.

Como essa docstring que tem algumas linhas há mais...
Aqui teremos uma descrição sobre o módulo. 
"""

def soma(x, y):
    """ Soma x e y
    
    Soma x e y 

    Args:
        x (int): Primeiro número
        y (int): Segundo número

    Returns:
        int: Retorna a soma de x e y.
    """
    return x + y


def multiplica(x, y, z=None):
    """
    Multiplica x, y e z.

    Multiplica x, y, z. O programador pode omitir o parâmetro z caso não tenha necessidade de usá-la.

    Args:
        x (int ou float): Número 1
        y (int ou float): Número 2
        z (int ou float, opcional): Número 3. O padrão é None.
    
    Returns:
        int ou float: A multiplicação de x, y e z         
    """
    
    
    if z: 
        return x * y * z
    else:
        return x * y



def texto(texto):
    """Função que exibe um texto.

    Args:
        texto (str): texto que será exibido

    Raises:
        TypeError: Se o texto não for uma string

    Returns:
        str: Retorna o texto
    """
    if not isinstance(texto, str):
        raise TypeError('Texto não é uma string.')
    
    return texto


class Operacoes:
    """Efetua algumas das operações matematicas.
    
    As operações disponível são Divisão e Ponteciação.
    """

    def __init__(self, x: float, y: float):
        """Inicializa os dados.

        Args:
            x (float): Primeiro número
            y (float): Segundo número
        """
        self.x = x
        self.y = y
    
    
    def divide(self):
        """Divide x por y

        Returns:
            float: A divisão de x por y
        """
        return self.x / self.y
    
    
    def pont(self):
        """Eleva x para y

        Returns:
            float: x elevado a y
        """
        return self.x ** self.y
