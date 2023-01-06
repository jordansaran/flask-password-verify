"""
Controllers(business role logic) Regras de negócio da API de validação de password
"""
import re
from re import Match

from src.api.verify.constants import ConstVerify
from src.api.verify.dataclasses import DcVerification, DcRule


class RulesRegexController:
    """
    Realiza a aplicação dos regex para validar o password.
    :param SEP: str - variável responsável por determinar um caracter de separação. O caracter é ponto e vírgula(;)
    :param dict_rules_regex: dict - Dicionário que contem como chave a regra o qual será aplicada para validar e, em
    sua estrutura interna contém o regex que será utilizada na validação e se esse regex contém um valor minímo
    de repetições que um caracter ou conjunto de caracteres deve existir no regex.
    """

    SEP = ';'
    __rules: list[DcRule]
    __dict_rules_regex: dict

    def __init__(self, rules: list[DcRule] = None):
        """
        :param rules: list[DcRules] contém um objeto de dataclass DcRule que possui
        a regra e valor para validar o password
        """
        self.__rules = rules
        self.__creating_dict_rules_regex()

    def __creating_dict_rules_regex(self) -> None:
        """
        Inserindo dados na variável dict_rules_regex.
        :return: None
        """
        self.__dict_rules_regex = {
            'minSize': {
                'regex': r"""[a-zA-z0-9!@#$%^&*()\-+\\/{}\[\]]{;,}""",
                'need_value': True
            },
            'minUppercase': {
                'regex': r"[A-Z]{;,}",
                'need_value': True
            },
            'minDigit': {
                'regex': r"[\d+]{;,}",
                'need_value': True
            },
            'minLowercase': {
                'regex': r"[a-z]{;,}",
                'need_value': True
            },
            'noRepeted': {
                'regex': r"^(?!.*([a-zA-z0-9!@#$%^&*()\-+\\/{}\[\]])\1{1,}).+$",
                'need_value': False
            },
            'minSpecialChars': {
                'regex': r"[!@#$%^&*()\-+\\/{}\[\]]{;,}",
                'need_value': True
            }
        }

    def __is_match(self,
                   password: str = None,
                   regex: str = None,
                   need_value: bool = False,
                   value: int = 0
                   ) -> Match[str] | None:
        """
        Valida se o password é valído a partir de um regex, caso ele sejá valído ele retorna None, caso contrário ele
        retorna um objeto Match contém os pontos que o regex encontrou
        :param password: str = None (Password que será avaliado)
        :param regex: str = None (regex que irá ser aplicado na validação do password)
        :param need_value: bool = None (Caso o regex contém uma condição que necessita de um valor mínimo de repetições
        de caracteres ou conjunto deles
        :param value: int = 0 (Passa o valor mínimo de repetições que o regex necessita)
        :return: Match[str] | None
        """
        if need_value:
            # Caso o regex necessita de um valor mínimo de repetições já partimos do presuposto que o regex internamente
            # possui o valor da variável "SEP", neste caso (;) e esse valor é subistuído pelo valor da variável "value"
            return re.search(regex.replace(self.SEP, str(value)), password)
        return re.search(regex, password)

    def to_verify_rules(self, password: str = None) -> list[str]:
        """
        Verifica o password a partir de um conjunto de regras
        :param password: str = None (Password que será avaliado)
        :return: list[str]
        """
        list_verify: list[str] = []
        for rule in self.__rules:
            # Verifica se no dicionário existe a respectiva regra que será utilizada para realizar a validação do
            # password caso ela existe a regra é aplicada ao password a partir do método is_match()
            rule_regex = self.__dict_rules_regex.get(rule.rule)
            if rule_regex is not None:
                # Caso a regra aplicada no password sejá None significa que o password não é válido para aquela regra
                # que foi utilizada para avaliar ele, sendo assim, o nome dessa regra é guardo em lista que recebe o
                # apenas o tipo string
                if self.__is_match(password=password,
                                   regex=rule_regex.get('regex'),
                                   need_value=rule_regex.get('need_value'),
                                   value=rule.value) is None:
                    list_verify.append(rule.rule)
        return list_verify


class VerificationController:

    __dc_verification: DcVerification | None
    __rules_regex_controller: RulesRegexController

    def __init__(self, payload: dict = None):
        if payload is not None:
            self.__dc_verification = DcVerification(password=payload.get(ConstVerify.PASSWORD),
                                                    rules=payload.get(ConstVerify.RULES))
            self.__rules_regex_controller = RulesRegexController(self.__dc_verification.rules)
        else:
            self.__dc_verification = None

    def execute(self):
        list_no_match = self.__rules_regex_controller.to_verify_rules(self.__dc_verification.password)
        return {'verify': False if len(list_no_match) > 0 else True, 'noMatch': list_no_match}
