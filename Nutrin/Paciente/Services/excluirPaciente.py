def excluirPaciente(username):
    from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPaciente
    paciente = pesquisarPaciente(username, True)
    if paciente:
        from Nutrin import db
        db.session.delete(paciente)
        db.session.commit()
        #from Nutrin.User.Services.excluirUser import excluirUser
        #excluirUser(username)
        return True
    return False
