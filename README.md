# Teste Técnico Academy

# Como usar o programa:
Para executar esse programa basta clonar esse repositório e executar a main.py em algum programa que suporte programaas em python (Pycharm, VSCode, Atom).

# Como o código funciona:

É chamado inicalmente a função setDoubles declarando as variáveis studentsVector e duos.

    def setDoubles():
    
      studentsVector = []
      duos = []

      for a in range(10):
          randomStudents(studentsVector)

      for b in range(10):
          defineMembers(studentsVector, duos)

      for pair in duos:
          print(pair)


Primeiramente é chamada o método randomStudents dentro de um laço o que fará este ser executada 10 vezes. Será passado para o método o vetor studentsVector,
do qual esse vetor guardará os alunos. No método Random Students será chamado inicialmente o médoto drawn students.
    
    def randomStudents(studentsVector):
      students = drawnStudents()
     ...
O método Drawn Students selecionará 2 alunos aleatórios do ciclo 1.

    def drawnStudents():
    
      student1 = cycle1["group" + str(random.randint(1, 5))][random.randint(0, 3)]
      student2 = cycle1["group" + str(random.randint(1, 5))][random.randint(0, 3)]
      return student1, student2

Após isso, em Random Students, é feita uma verificação se esses dois alunos selecionados são diferentes. Caso sejam, é feita outra verificação checando se o vetor
studentsVector está vazio, se estiver o vetor receberá os valores de student. Se o vetor studentsVector não estiver vazio, é verificado se os alunos selecionados já
estão inseridos no vetor. Caso não estejam, esses alunos seram incluídos no vetor. Caso os alunos selecionados inicialmente sejam iguais ou se os alunos já estiverem
inseridos em studentVector é feito uma recursividade chamando novamente o método RandomStudents 
    
    def randomStudents(studentsVector):

      students = drawnStudents()

      if students[0] != students[1]:
        if len(studentsVector) == 0:
            studentsVector.append(students[0])
            studentsVector.append(students[1])

        else:
            if students[0] not in studentsVector and students[1] not in studentsVector:
                studentsVector.append(students[0])
                studentsVector.append(students[1])
            else:
                randomStudents(studentsVector)
      else:
        randomStudents(studentsVector)
       
Após ter populado o vetor studentsVector, em setDoubles é executado o segundo laço chamando a função Define Members passando o vetor studentsVector já populado
e a variável duo. Agora em defineMembers, inicialmente é chamado o método get_two_students e para esse método é passado studentsVector.

      def defineMembers(studentsVector, duos):
        students = get_two_students(studentsVector)
 
No método get_two_students é selecionado dois alunos de forma aleatória de studentVector.
    def get_two_students(studentsVector):

      member1 = studentsVector[random.randint(0, 19)]
      member2 = studentsVector[random.randint(0, 19)]
  
      return member1, member2
      
Depois disso, em defineMembers é feita uma verificação se os alunos selecionados são diferentes. Caso sejam, é verificado se a variável duo, que é um array, está vazia.
Uma vez estando vazia é chamado o método checking cycles.

      def defineMembers(studentsVector, duos):
        students = get_two_students(studentsVector)
        if students[0] != students[1]:
          if len(duos) == 0:
            checkCycle = checkingCycles(students)
           
Em checkingCycles é verificado se os alunos selecionados não já estiveram em um grupo nos ciclos anteriores. O método retornará um valor falso caso os alunos já tenham
estado na mesma equipe, e um valor verdadeiro caso contrário.
      
      def checkingCycles(students):
      
        cycles = [cycle1, cycle2]
        check = True
        for cycle in cycles:
            for group, valor in cycle.items():
                if students[0] in cycle[group] and students[1] in cycle[group]:
                    check = False
        return check

Se o valor retornado for True então os valores de students serão inseridos em duos através do método registerDuo, caso contrário, o método defineMembers é chamado novamente
        
      def defineMembers(studentsVector, duos):
        students = get_two_students(studentsVector) 
          if students[0] != students[1]:
            if len(duos) == 0:
                checkCycle = checkingCycles(students)
                if checkCycle:
                    registerDuo(duos, students)
                else:
                    defineMembers(studentsVector, duos)

Agora caso duos não esteja vazio, é chamado o método pairChecking.
      
      def defineMembers(studentsVector, duos):
        students = get_two_students(studentsVector) 
          if students[0] != students[1]:
            if len(duos) == 0:
                checkCycle = checkingCycles(students)
                if checkCycle:
                    registerDuo(duos, students)
                else:
                    defineMembers(studentsVector, duos)
            else:
                pairCheck = pairChecking(duos, students)

O método pairChecking checa se os alunos selecionados já estão inseridos no array duos, caso esteja é retornado false, do contrário é retornado true.
       
       def pairChecking(duos, students):
       
          for pair in duos:
            if students[0] in pair or students[1] in pair:
              return False
          return True

Caso o retorno seja True é repetido o processo do checkCycles, onde caso passe é inserido os alunos em duo, caso contrário é chamado novamente defineMembers. Se o
retorno for False então é chamado diretamente a função defineMembers.
    
    def defineMembers(studentsVector, duos):
    
      students = get_two_students(studentsVector)

      if students[0] != students[1]:
          if len(duos) == 0:
              checkCycle = checkingCycles(students)
              if checkCycle:
                  registerDuo(duos, students)
              else:
                  defineMembers(studentsVector, duos)
          else:
              pairCheck = pairChecking(duos, students)
              if pairCheck:
                 checkCycle = checkingCycles(students)
                  if checkCycle:
                      registerDuo(duos, students)
                 else:
                      defineMembers(studentsVector, duos)
              else:
                  defineMembers(studentsVector, duos)
      else:
          defineMembers(studentsVector, duos)

Por fim em setDoubles os valores de duo são impressos.
      
      for pair in duos:
          print(pair)







