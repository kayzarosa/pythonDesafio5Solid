from abc import ABC, abstractmethod


# Interface (classe abstrata) para exames
class ValidadorExame(ABC):
    @abstractmethod
    def validar(self) -> bool:
        pass


# Implementação específica para exame de sangue
class ValidadorExameSangue(ValidadorExame):
    def validar(self) -> bool:
        # Implementar regras específicas para validação de exame de sangue
        print("Validando exame de sangue...")
        return True


# Implementação específica para exame de raio-x
class ValidadorExameRaioX(ValidadorExame):
    def validar(self) -> bool:
        # Implementar regras específicas para validação de raio-x
        print("Validando exame de raio-x...")
        return True


# Classe que representa um exame
class Exame:
    def __init__(self, tipo: str, validador: ValidadorExame):
        self.tipo = tipo
        self.validador = validador


# Classe que aprova exames
class AprovadorExame:
    def aprovar_solicitacao_exame(self, exame: Exame) -> bool:
        if exame.validador.validar():
            print(f"Exame de {exame.tipo} aprovado!")
            return True
        print(f"Exame de {exame.tipo} reprovado!")
        return False


# Exemplo de uso:
if __name__ == "__main__":
    # Criando exames com seus respectivos validadores
    exame_sangue = Exame("sangue", ValidadorExameSangue())
    exame_raio_x = Exame("raio-x", ValidadorExameRaioX())

    # Aprovando exames
    aprovador = AprovadorExame()
    aprovador.aprovar_solicitacao_exame(exame_sangue)
    aprovador.aprovar_solicitacao_exame(exame_raio_x)
