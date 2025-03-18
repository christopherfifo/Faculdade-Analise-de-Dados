class  Endereco():
    def setLogradouro(self, logradouro):
        self.logradouro = logradouro
    
    def setNumero(self, num = 's/n'):
        self.num = num
    
    def setBairro(self, bairro):
        self.bairro = bairro
    
    def setCidade(self, cidade):
        self.cidade = cidade
    
    def setEstado(self, estado):
        self.estado = estado

    def __str__(self):
        return self.logradouro + ', ' + str(self.num) + ' - ' + self.bairro + ' - ' + self.cidade + ' - ' + self.estado  