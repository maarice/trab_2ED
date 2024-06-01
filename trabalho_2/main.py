class Estudante_indigena:
    def __init__(self, nome, povos_indigenas, universidade, curso, ano_formacao):
        self.nome = nome
        self.povos_indigenas = povos_indigenas
        self.universidade = universidade
        self.curso = curso
        self.ano_formacao = ano_formacao

    def __str__(self):
        return (f'NOME: {self.nome}, POVO INDÍGENA PERTECENTE: {self.povos_indigenas}, UNIVERSIDADE: {self.universidade}, '
        f'CURSO: {self.curso}, ANO FORMAÇÃO: {self.ano_formacao}')

class Noh:
    def __init__(self, estudante):
        self.estudante = estudante
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir_estudante(self, estudante):
        if self.raiz is None:
            self.raiz = Noh(estudante)
        else:
            self.tamanho_nome(self.raiz, estudante)
    
    def tamanho_nome(self, noh_atual, estudante):
        if estudante.nome < noh_atual.estudante.nome:
            if noh_atual.esquerda is None:
                noh_atual.esquerda = Noh(estudante)
            else:
                self.tamanho_nome(noh_atual.esquerda, estudante)
        else:
            if noh_atual.direita is None:
                noh_atual.direita = Noh(estudante)
            else:
                self.tamanho_nome(noh_atual.direita, estudante)
    
    def buscar_estudante(self, nome):
        return self.buscar_nome(self.raiz, nome)

    def buscar_nome(self, noh_atual, nome):
        if noh_atual is None or noh_atual.estudante.nome == nome:
            return noh_atual
        if nome < noh_atual.estudante.nome:
            return self.buscar_nome(noh_atual.esquerda, nome)
        return self.buscar_nome(noh_atual.direita, nome)

    def remover_estudante(self, nome):
        self.raiz = self.remover(self.raiz, nome)

    def remover(self, noh_atual, nome):
        if noh_atual is None:
            return noh_atual
        if nome < noh_atual.estudante.nome:
            noh_atual.esquerda = self.remover(noh_atual.esquerda, nome)
        elif nome > noh_atual.estudante.nome:
            noh_atual.direita = self.remover(noh_atual.direita, nome)
        else:
            if noh_atual.esquerda is None:
                return noh_atual.direita
            elif noh_atual.direita is None:
                return noh_atual.esquerda
            menor_valor = self._min_valor_noh(noh_atual.direita)
            noh_atual.estudante = menor_valor.estudante
            noh_atual.direita = self._remover(noh_atual.direita, menor_valor.estudante.nome)
        return noh_atual
        
    def _min_valor_noh(self, noh):
        atual = noh
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def atualizar_estudante(self, nome, novos_dados):
        noh = self.buscar_estudante(nome)
        if noh:
            noh.estudante.nome = novos_dados.get('nome', noh.estudante.nome)
            noh.estudante.povos_indigenas = novos_dados.get('povos_indigenas', noh.estudante.povos_indigenas)
            noh.estudante.universidade = novos_dados.get('universidade', noh.estudante.universidade)
            noh.estudante.curso = novos_dados.get('curso', noh.estudante.curso)
            noh.estudante.ano_formacao = novos_dados.get('ano_formacao', noh.estudante.ano_formacao)

    def mostrar_ordem_estudantes(self):
        self.mostrar_ordem(self.raiz)

    def mostrar_ordem(self, noh_atual):
        if noh_atual is not None:
            self.mostrar_ordem(noh_atual.esquerda)
            print(noh_atual.estudante)
            self.mostrar_ordem(noh_atual.direita)
    
    def buscar_povos_indigenas(self, povos_indigenas):
        return self.buscar_povos_indigenas_existente(self.raiz, povos_indigenas)
    
    def buscar_povos_indigenas_existente(self, noh_atual, povos_indigenas):
        if noh_atual is not None or noh_atual.estudante.povos_indigenas == povos_indigenas:
            return noh_atual
        if povos_indigenas < noh_atual.estudante.povos_indigenas:
            return self.buscar_povos_indigenas_existente(noh_atual.esquerda, povos_indigenas)
        return self.buscar_povos_indigenas_existente(noh_atual.direita, povos_indigenas)    

    def buscar_universidade(self, universidade):
        busca_universidade = []
        self.buscar_universidade_existente(self.raiz, universidade, busca_universidade)
        return busca_universidade
    
    def buscar_universidade_existente(self, noh_atual, universidade, busca_universidade):
        if noh_atual is not None:
            if noh_atual.estudante.universidade == universidade:
                busca_universidade.append(noh_atual.estudante)
            self.buscar_universidade_existente(noh_atual.esquerda, universidade, busca_universidade)
            self.buscar_universidade_existente(noh_atual.direita, universidade, busca_universidade)

def menu_sistema():
    arvore = ArvoreBST()
    continuar = True

    while continuar:
        print('\nMenu Principal:')
        print('1. Adicionar aluno')
        print('2. Buscar Aluno por nome')
        print('3. Buscar Aluno por Povos Indígenas')
        print('4. Exibir Alunos por Universidade')
        print('5. Exibir todos os alunos (em ordem)')
        print('6. Remover Aluno')
        print('7. Atualizar informações do estutande')
        print('8. Sair')

        escolha = input('Escolha uma das opções: ')

        if escolha == '1':
            nome = input('Nome do estudante: ').upper()
            povos_indigenas = input('Qual grupo indígena pertencente: ').upper()
            universidade = input('Universidade (nome por extenso): ').upper()
            curso = input('Curso: ').upper()
            
            while True:
                ano_formacao = input('Formação: ')
                if ano_formacao.isdigit():
                    ano_formacao = int(ano_formacao)
                    break
                else:
                    print('Por favor, ensira somente números para o ano de formação.')

            estudante = Estudante_indigena(nome, povos_indigenas, universidade, curso, ano_formacao)
            arvore.inserir_estudante(estudante)

        elif escolha == '2':
            nome = input('Nome: ').upper()
            busca_nome = arvore.buscar_estudante(nome)
            if busca_nome:
                    print(busca_nome.nome)
            else:
                print('Aluno não encontrado.')

        elif escolha == '3':
            povos_indigenas = input('Povos Indígenas: ').upper()
            busca_povos_indigenas = arvore.buscar_povos_indigenas(povos_indigenas)
            if busca_povos_indigenas:
                for povos_indigenas_existente in busca_povos_indigenas:
                    print(povos_indigenas_existente)
            else:
                print('Nenhum aluno encontrado com esses povos indígenas.')
            
        elif escolha == '4':
            universidade = input('Universidade: ').upper()
            busca_universidade = arvore.buscar_universidade(universidade)
            if busca_universidade:
                for universidade_existente in busca_universidade:
                    print(universidade_existente)
            else:
                print('Nenhum aluno encontrado com vínculo nessa Universiade ') 
        
        elif escolha == '5':
            arvore.mostrar_ordem_estudantes()

        elif escolha == '6':
            nome = input('Nome do estudante a ser removido: ').upper()
            arvore.remover_estudante(nome)
            print('Estudante removido.')

        elif escolha == '7':
            nome = input('Nome do estudante a ser atualizado: ').upper()
            novos_dados = {}
            atualizar = input('Deseja atualizar o nome? (s/n): ').lower()
            if atualizar == 's':
                novos_dados['nome'] = input('Novo nome: ').upper()
            atualizar = input('Deseja atualizar povos indígenas? (s/n): ').lower()
            if atualizar == 's':
                novos_dados['povos_indigenas'] = input('Novo povo indígena: ').upper()
            atualizar = input('Deseja atualizar universidade? (s/n): ').lower()
            if atualizar == 's':
                novos_dados['universidade'] = input('Nova universidade: ').upper()
            atualizar = input('Deseja atualizar curso? (s/n): ').lower()
            if atualizar == 's':
                novos_dados['curso'] = input('Novo curso: ').upper()
            atualizar = input('Deseja atualizar ano de formação? (s/n): ').lower()
            if atualizar == 's':
                while True:
                    ano_formacao = input('Novo ano de formação: ')
                    if ano_formacao.isdigit():
                        novos_dados['ano_formacao'] = int(ano_formacao)
                        break
                    else:
                        print('Por favor, insira somente números para o ano de formação.')
            arvore.atualizar_estudante(nome, novos_dados)
            print(f'Aluno {nome} atualizado.')
        
        elif escolha == '8':
            continuar = False
        
        else:
            print('Opção inválida, tente novamente.')

if __name__ == '__main__':
    menu_sistema()