enum class Nivel { BASICO, INTERMEDIARIO, DIFICIL }

class Usuario

data class ConteudoEducacional(var nome: String, val duracao: Int = 60)

data class Formacao(val nome: String, var conteudos: List<ConteudoEducacional>) {
    val inscritos = mutableListOf<Usuario>()

    fun matricular(usuario: Usuario) {
        inscritos.add(usuario) // Simula a matrícula adicionando o usuário à lista de inscritos
    }
}

fun main() {
    val usuario1 = Usuario()
    val usuario2 = Usuario()

    val conteudo1 = ConteudoEducacional("Introdução ao Kotlin")
    val conteudo2 = ConteudoEducacional("Programação Orientada a Objetos", duracao = 90)

    val formacao = Formacao("Formação em Kotlin", listOf(conteudo1, conteudo2))
    formacao.matricular(usuario1) // Simula a matrícula do usuário 1 na formação
    formacao.matricular(usuario2) // Simula a matrícula do usuário 2 na formação

    println("Inscritos na formação: ${formacao.inscritos}")
}
