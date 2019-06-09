# Tropas #
Projeto iniciado com o intuito de dividir "automaticamente" tropas para o jogo ROK

## To do ##  
1. **Divisão**
    * Não simplesmente fazer a divisão dando prioridade para o primeiro comandante utilizando a seguinte fórmula, comandates[0] = ("tropas[j]"//quantidade\_comandantes + "tropas[j]"%quantidade\_comandantes) e os demais recebem comandantes[i] = ("tropas[j]"//quantidade\_comandantes"), utilizando divisão de inteiro em todos e deixando que o primeiro fique com resto da divisão. 
    * Forma a ser implementada: Tentar a Divisão levando em consideração o poder das tropas (que é basicamente o nível) por exemplo: na divisão inteira sobram cinco tropas lvl 1, duas lvl 2 e uma lvl 3 e têm-se três comandantes, o todos vão receber 4 de poder ainda ex:
```python
# Isto está mais para um pseudo código, pois só está aqui para deixar a ideia geral
comandantes[0].tropas[j].set_poder(comandantes[0].tropas[j].get_poder()+(uma tropa lvl3+uma lvl1))
comandantes[1].tropas[j].set_poder(comandantes[1].tropas[j].get_poder()+(duas tropas lvl 2))
comandantes[2].tropas[j].set_poder(comandantes[2].tropas[j].get_poder()+(quatro tropas lvl 1))
# Porém se houver um caso o primeiro comandante ainda terá prioridade.
```
2. **Reconhecimento de voz:**
    * Utilizar as bibliotecas:
      * Reconhecimento de voz
        * SpeechRecognition
        * pyaudio
      * Para "falar":
        * gTTS
        * pyttsx3
        * playsound

Utilizar o reconhecimento de voz para auxiliar com comandos como por exemplo:
"Quantidade de arqueiros nivel 1 para o primeiro comandante"
E então será reconhecido e se tiver algum arqueiro de nivel 1 será dito:
"Existem N arqueiros nivel 1 para o primeiro comandante, N"
Sendo N a quantidade de arqueiros.
### Ferramentas utilizadas ###
[Python](https://www.python.org/) - Interpretador Python versão 3.7.3
**Bibliotecas Python:**
* [gTTS](https://pypi.org/project/gTTS/) - (Google Text-To-Speech) biblioteca para conversão de texto para voz.
* [playsound](https://pypi.org/project/playsound/) - Biblioteca para tocar sons (multiplataforma).
* [PyAudio](https://pypi.org/project/PyAudio/) - Biblioteca para saída/entrada de aúdio multiplataforma.
* [pyttsx](https://pypi.org/project/pyttsx3/) - Biblioteca para conversão de texto em voz que funciona offline.
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Biblioteca para reconhecimento de voz(online e offline).