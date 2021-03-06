from Nutrin import db
from TipoAtendimento import TipoAtendimento
from Antropometria import Antropometria
from TipoEstado import TipoEstado
from Nutrin.Paciente.Model.Paciente import Paciente

class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    tipoAtendimento_id = db.Column(db.Integer, db.ForeignKey('tipoAtendimentos.id'), nullable=False)
    hora = db.Column(db.TIME, nullable=False)
    data = db.Column(db.Date, nullable=False)
    tipoEstado_id = db.Column(db.Integer, db.ForeignKey('tipoEstados.id'), nullable=False)
    antropometria_id = db.Column(db.Integer, db.ForeignKey('tipoAtendimentos.id'))
    dieta = db.Column(LargeBinary)
    pagamento = db.Column(Boolean, default=False)

    def __init__(self, paciente_id, tipoAtendimento_id, hora, data, tipoEstado_id):
        self.paciente_id = paciente_id
        self.tipoAtendimento_id = tipoAtendimento_id
        self.hora = hora
        self.data = data
        self.tipoEstado_id = tipoEstado_id
    

    def __repr__(self):
        return "<Consulta {}".format(self.tipoEstado_id)


    
