#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re


# ===================================================================================
# 1. DICIONÁRIO DE DADOS BRUTOS (EXPANDIDO)
# ===================================================================================
nlu_dataset_bruto = {
    "saudacao": {
        "examples": [
            "Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "E aí, tudo bem?",
            "Opa, como vai?", "Oi, preciso de uma informação", "Gostaria de começar o atendimento",
            "Podemos começar?", "Quero iniciar uma conversa", "Olá, tem alguém aí para me ajudar?",
            "Preciso de suporte", "Ei, bom dia", "Boa tarde, poderiam me auxiliar?",
            "Alô, preciso de ajuda", "Como posso ser ajudado?", "Olá, preciso de um auxílio",
            "Oi, como você está?", "Saudações", "Como vai?", "Quero falar com vocês",
            "Olá, equipe", "Oi, tudo certo?", "Bom dia, gostaria de um suporte",
            "Boa noite, tudo bom?", "Hey", "Posso fazer uma pergunta?",
            "Iniciar atendimento", "Oi, pode me ajudar?", "Começar", "Início",
            "Bom dia, preciso de informações", "Boa tarde, quero tirar uma dúvida",
            "Olá, boa noite, como estão?", "E aí", "Opa", "Começar chat",
            "Preciso de ajuda com um pedido", "Quero saber sobre um produto", "Olá, me ajude por favor",
            "Alô, tem alguém online?", "Gostaria de um auxílio", "Oi, bom dia!",
            "E aí, beleza?", "Boa tarde, equipe", "Boa noite, preciso de suporte técnico",
            "Olá, meu amigo", "Quero começar a conversa", "Poderia me dar uma mão?",
            "Start", "Preciso de um help", "Olá, gostaria de assistência",
            "Oi, tem alguém aí?", "Tudo bem com vocês?", "Como posso iniciar?",
            "Olá, como vai?", "Preciso falar com um atendente", "Oi, suporte",
            "Bom dia, tudo joia?", "Boa tarde, por favor, me ajude", "Boa noite, uma informação, por favor",
            "E aí, firmeza?", "Opa, bão?", "Olá, pessoal",
            "Como vai você?", "Posso começar?", "Quero ajuda",
            "Olá, preciso de ajuda com uma compra", "Oi, como faço para...", "Bom dia, gente",
            "Boa tarde, caros", "Boa noite, prezados", "Olá, tudo em ordem?",
            "Saudações, equipe de suporte", "Preciso de um help aqui", "Oi, me dá uma luz",
            "Bom dia, poderiam me ajudar?", "Boa tarde, como vai o atendimento?",
            "Boa noite, tem alguém para conversar?", "Olá, preciso de um esclarecimento",
            "Oi, como proceder?", "Gostaria de saber mais sobre...", "Olá, olá",
            "Quero atendimento", "Como estão?", "Olá, bom dia, tudo bem?",
            "Oi, boa tarde, preciso de ajuda", "Boa noite, gostaria de uma informação",
            "E aí, como andam as coisas?", "Opa, posso perguntar?", "Iniciando o contato",
            "Olá, equipe de atendimento", "Oi, pode me dar uma força?", "Bom dia, amigo(a)",

        ]
    },
    "despedida": {
        "examples": [
            "Tchau", "Até mais", "Até logo", "Obrigado, por enquanto é só", "Adeus",
            "Falou", "Tenha um bom dia", "Obrigado, pode encerrar", "Finalizar conversa",
            "Era só isso, obrigado(a)", "Não preciso de mais nada", "Por hoje é só",
            "Tudo resolvido, tchau", "Pode finalizar o atendimento, por favor",
            "Até a próxima", "Agradeço e até mais", "Tchau, tchau", "Encerrado, obrigado",
            "Fim de atendimento", "Obrigado pela ajuda, adeus", "Vou indo, até mais",
            "Bom trabalho e até a próxima", "Tenha uma ótima noite", "Grato, pode finalizar",
            "Já me ajudou, tchau", "É só isso", "Concluído, até logo", "Bye",
            "See you later", "Perfeito, pode encerrar", "Finalizar", "Encerrar",
            "Obrigado, tchau", "Até mais ver", "Tudo certo, pode finalizar",
            "Agradecido, até a próxima", "Pode fechar o chat", "Não tenho mais dúvidas, obrigado",
            "Resolvido, até mais", "Por mim, tudo bem, pode encerrar", "Tchau, obrigado",
            "Vou nessa", "Fui", "Até breve", "Tenha um bom resto de dia",
            "Obrigado e boa noite", "Finalizando...", "Pode concluir",
            "Era isso, valeu", "Nada mais, agradeço", "Por agora é só",
            "Tudo ok, tchau", "A conversa pode ser finalizada", "Obrigado, adeus",
            "Abraço e até mais", "Missão cumprida, tchau", "Pode encerrar, por favor",
            "Agradeço, pode finalizar", "Ok, pode encerrar", "Sem mais perguntas, obrigado",
            "É o suficiente, tchau", "Chega por hoje", "Fim de papo",
            "Obrigado, tenha um ótimo dia", "Pode finalizar a sessão",
            "Já tiraram minha dúvida, até mais", "Tudo esclarecido, tchau",
            "Obrigado, bom trabalho", "Isso conclui meu atendimento", "Ok, fim",
            "Tudo resolvido, pode fechar", "Agradeço o suporte, até mais",
            "Tchau e obrigado", "Flw", "Até logo, obrigado", "Perfeito, era só isso",
            "Pode dar como encerrado", "Obrigado, vou indo", "Chegamos ao fim",
            "Por hoje chega", "Obrigado pela assistência, tchau", "Até, obrigado",
            "Concluído com sucesso, adeus", "Pode finalizar, agradecido",
            "Ok, tchau", "Tudo certo, até mais", "Obrigado, pode fechar",
            "Encerre o atendimento, por favor", "Valeu, até a próxima",
            "Isso é tudo, tchau", "Grato, até logo", "Finalizar chat",
            "Pode me desconectar", "Obrigado e até mais", "Era só essa a questão, tchau",
            "Não necessito de mais nada, obrigado", "Obrigado, tenha uma boa tarde",
            "Finalizado", "Pode fechar a conversa", "Tchau, se cuida",
            "Até mais, obrigado pela ajuda", "Por mim, encerramos", "Valeu, falou",
        ]
    },
    "agradecimento": {
        "examples": [
            "Obrigado", "Obrigada", "Valeu", "Grato(a)", "Muito obrigado(a)",
            "Agradeço a ajuda", "Show, valeu", "Perfeito, obrigado", "Excelente, muito obrigado",
            "Obrigado pela informação", "Agradeço a atenção", "Valeu pelo suporte",
            "Ajudou demais, obrigado", "Minha dúvida foi sanada, grato", "Resolvido, obrigado!",
            "Obrigadão", "Agradecido(a)", "Valeu mesmo", "Fico muito grato(a)",
            "Show de bola, obrigado", "Satisfeito, obrigado", "Muito bom, valeu",
            "Ok, agradeço", "Entendi, muito obrigado", "Ótimo, era isso. Obrigado",
            "Maravilha, valeu!", "Gratidão", "Thanks", "Tks", "Obrigado pela paciência",
            "Agradeço imensamente", "Muito agradecido", "Valeu pela força", "Obrigado pelo esclarecimento",
            "Agradeço de coração", "Top, obrigado", "Excelente, agradeço", "Obrigado, você me ajudou muito",
            "Grato pela resposta rápida", "Valeu, fera", "Obrigado, amigo(a)", "Agradeço o retorno",
            "Muito obrigado pelo auxílio", "Fico agradecido", "Obrigado pelo tempo", "Agradecido pela ajuda",
            "Que bom, obrigado", "Muitíssimo obrigado", "Ok, valeu", "Obrigado pela assistência",
            "Ajudou bastante, obrigado", "Esclarecido, obrigado", "Obrigado pela dica",
            "Genial, obrigado", "Agradeço a gentileza", "Obrigado pelo excelente atendimento",
            "Valeu, nota 10", "Tudo certo, obrigado", "Obrigado, foi de grande ajuda", "Sou grato",
            "Agradeço a presteza", "Obrigado pelo help", "Valeu pela moral", "Obrigado por tudo",
            "Isso mesmo, obrigado", "Perfeito, agradeço", "Obrigado, era o que eu precisava",
            "Maravilha, obrigado", "Obrigado pela colaboração", "Grato pelo apoio",
            "Obrigado, Deus lhe pague", "Agradeço muito", "Valeu, de verdade",
            "Obrigado pela clareza", "Agradecido, amigo", "Obrigado, resolveu meu problema",
            "Show, muito obrigado", "Ok, grato", "Obrigado pelo suporte técnico",
            "Agradeço o esforço", "Obrigado, você é um anjo", "Era isso, valeu mesmo",
            "Obrigado, foi ótimo", "Grato pela atenção dispensada", "Valeu a pena, obrigado",
            "Obrigado pela ajuda rápida", "Agradeço a explicação", "Obrigado pela orientação",
            "Fico grato", "Valeu, campeão", "Obrigado, isso ajuda muito", "Agradeço sua ajuda",
            "Excelente suporte, obrigado", "Obrigado por me ajudar", "Grato pela informação",
            "Obrigado, foi muito útil", "Valeu pela ajuda, de verdade", "Agradeço sinceramente",
            "Muito obrigado, de verdade", "Top, valeu", "Obrigado, foi um prazer",
            "Agradecido pela paciência", "Obrigado, foi mais fácil do que eu pensava",
        ]
    },
    "afirmacao": {
        "examples": [
            "Sim", "Ok", "Certo", "Correto", "Exato", "Isso mesmo", "Com certeza",
            "Claro", "Positivo", "Afirmativo", "Confirmo", "De acordo", "Beleza",
            "Fechado", "Combinado", "Sim, por favor", "Sim, gostaria",
            "Isso, pode continuar", "Exatamente isso", "Concordo", "Pode ser",
            "Aham", "Uhum", "É isso aí", "Pode prosseguir", "Está correto",
            "Isso", "Yep", "S", "Sim, eu quero", "Pode crer", "Justo", "Sem dúvida",
            "Claro que sim", "É isso", "Certíssimo", "Corretíssimo", "Exatamente",
            "Isso, por favor", "Sim, pode ser", "Com certeza absoluta", "Pode confirmar",
            "Estou de acordo", "Feito", "Tá certo", "É isso mesmo", "Ok, pode ir em frente",
            "Beleza então", "Sim, prossiga", "Confirmo a informação", "Isso, pode fazer",
            "Correto, é essa a opção", "Sim, aceito", "Positivo, pode continuar", "Ok, entendi",
            "Certo, pode ser", "Com certeza, vamos lá", "Claro, por que não?", "Afirmativo, capitão",
            "De acordo total", "Fechou", "Tá combinado", "Sim, por gentileza",
            "Isso, pode mandar bala", "Exato, é isso que eu quero", "Concordo plenamente",
            "Pode ser sim", "Uhum, pode continuar", "É exatamente isso", "Pode seguir",
            "Está certíssimo", "Isso aí", "Sim, quero sim", "Pode apostar que sim",
            "Sem dúvidas", "Claro, pode fazer", "Positivo e operante", "Confirmo, pode prosseguir",
            "De acordo, vamos em frente", "Beleza pura", "Fechado, negócio fechado", "Combinadíssimo",
            "Sim, por favor, continue", "Sim, gostaria muito", "Isso, continue por favor",
            "Exatamente isso que eu pensei", "Concordo com você", "Pode ser uma boa",
            "Aham, prossiga", "Uhum, isso mesmo", "É isso aí, pode continuar", "Pode prosseguir, por favor",
            "Está correto, pode avançar", "Isso, por favor, faça", "Sim, eu desejo", "Certamente",
            "Óbvio", "Claro que pode", "Pode mandar ver", "Ok, confirmado",
            "Sim, está certo", "Pode ir", "Okay", "S, pfv", "Isso.", "Exato.",
        ]
    },
    "negacao": {
        "examples": [
            "Não", "Negativo", "De jeito nenhum", "Jamais", "Errado", "Incorreto",
            "Não, obrigado(a)", "Não quero", "Não, não é isso", "Absolutamente não",
            "Claro que não", "Nem pensar", "De forma alguma", "Não, pode cancelar",
            "Não concordo", "Discordo", "Não é verdade", "Acho que não", "Desta vez não",
            "Agora não", "Ainda não", "Não tenho interesse", "Impossível", "Sem chances",
            "Não, está errado", "Não, essa não é a informação correta",
            "Não, não foi o que eu perguntei", "Nope", "N", "De maneira nenhuma", "Nop",
            "Não, de jeito nenhum", "Jamais, em tempo algum", "Incorreto, pode corrigir", "Não, valeu",
            "Não gostaria", "Não, isso está incorreto", "Nada disso", "Claro que não, pode parar",
            "Nem pensar nisso", "De forma alguma, cancele", "Não, não concordo com isso",
            "Discordo totalmente", "Isso não é verdade", "Creio que não", "Hoje não",
            "Nesse momento não", "Ainda não, obrigado", "Não possuo interesse", "É impossível",
            "Nenhuma chance", "Não, a informação está errada", "Não foi isso que eu disse",

            "Não, você entendeu errado", "De maneira alguma", "Não mesmo", "Nem vem",
            "Nada feito", "Não, por favor, pare", "Não, não quero", "Errado, não é essa opção",
            "Não, obrigado, dispenso", "Não estou interessado", "Não, não é o que eu busco",
            "Absolutamente incorreto", "Claro que não, está louco?", "Nem em sonho",
            "De jeito algum", "Não, cancele por favor", "Não estou de acordo", "Discordo veementemente",
            "Isso é falso", "Acho que não é por aí", "Desta vez passo", "Agora não, por favor",
            "Ainda não é o momento", "Sem interesse", "Completamente impossível",
            "Chance zero", "Não, está tudo errado", "Não, a informação correta é outra",
            "Não foi essa a minha pergunta", "Não, não, não", "Nananinanão", "Nem a pau",
            "De modo algum", "Não, pode deixar", "Não, não precisa", "Não quero, obrigado",
            "Incorreto, verifique novamente", "Não, não é isso que eu preciso", "Absolutamente não, pare",

            "Nem pense nisso", "De forma alguma, não continue", "Não, discordo",
            "Isso é mentira", "Acho que não, hein", "Desta vez não, obrigado",
            "Agora não dá", "Ainda não, quem sabe depois", "Não tenho o menor interesse",
            "Isso é impossível de fazer", "Sem a menor chance", "Não, está incorreto",
            "Não, a informação está equivocada", "Não, você não respondeu o que eu perguntei",
            "De jeito maneira", "Não, para", "Não, obrigado, de verdade", "Não quero, valeu",
        ]
    },
    "perguntar_horario_funcionamento": {
        "examples": [
            "Qual é o horário de funcionamento?", "A que horas vocês abrem?", "Quando a loja fecha?",
            "Até que horas o atendimento funciona?", "Vocês estão abertos agora?",
            "Qual o horário de atendimento hoje?", "Vocês abrem aos sábados?",
            "E no domingo, qual o horário?", "A loja funciona em feriados?",
            "Me informe o horário de vocês, por favor", "Gostaria de saber o horário de atendimento.",
            "A loja física abre em que horário?", "O atendimento por telefone tem horário específico?",
            "Qual o horário do suporte?", "O horário é o mesmo para todas as filiais?",
            "Poderia confirmar o horário de funcionamento?", "A loja já abriu?",
            "Ainda dá tempo de ir na loja?", "Vocês fecham para almoço?",
            "Qual o horário comercial de vocês?", "A que horas começa o atendimento?",
            "Até que horas posso ser atendido?", "Qual o horário de funcionamento da loja do shopping?",
            "O horário no site está atualizado?", "Qual o horário de funcionamento durante a semana?",
            "E no final de semana, como funciona?", "Preciso saber o horário para me programar.",
            "A que horas o expediente se encerra?", "Qual o horário da loja hoje?",
            "Amanhã vocês abrem em que horário?", "Qual o horário de funcionamento de segunda a sexta?",
            "A que horas fecham no sábado?", "A loja está aberta neste momento?",
            "O atendimento presencial vai até que horas?", "Me diga o horário de abertura e fechamento.",
            "Qual o horário de funcionamento da filial do centro?", "Vocês têm horário estendido?",
            "O horário de atendimento online é 24h?", "Qual o horário para retirada de produtos?",
            "Posso ir aí às 19h?", "A loja abre no próximo feriado?", "Qual o horário de funcionamento no Natal?",
            "E no Ano Novo, qual o horário?", "Gostaria de saber o horário de funcionamento da loja.",
            "A que horas o suporte por chat fica disponível?", "O horário da loja do bairro X é qual?",
            "Confirma pra mim o horário de funcionamento.", "Até quando a loja fica aberta hoje?",
            "Vocês abrem no período da manhã?", "E à tarde, até que horas vão?",
            "O expediente começa a que horas?", "O horário de atendimento telefônico é o mesmo da loja física?",
            "Qual o horário de vocês na sexta-feira?", "A que horas a loja fecha hoje?",
            "Qual o horário de pico no atendimento?", "Vocês funcionam em horário de almoço?",
            "Amanhã é feriado, vocês abrem?", "Qual o horário de atendimento do SAC?",
            "A loja física fecha a que horas?", "Posso ligar para vocês a que horas?",
            "O horário de funcionamento é padrão para todas as lojas?", "Me passa o horário, por favor.",
            "Gostaria de confirmar o horário.", "A que horas posso visitar a loja?",
            "Qual o horário de funcionamento para devoluções?", "O horário da assistência técnica é qual?",
            "A loja da zona sul abre que horas?", "Vocês trabalham aos domingos?",
            "Qual o horário no feriado de Corpus Christi?", "O horário de funcionamento mudou?",
            "Onde encontro o horário de funcionamento de vocês?", "Qual o horário de atendimento no balcão?",
            "A loja abre antes das 9h?", "O fechamento é às 18h mesmo?",
            "Qual o horário de atendimento especial de fim de ano?", "Vocês abrem no carnaval?",
            "A que horas o atendimento se inicia?", "Até que horas posso resolver meu problema hoje?",
            "Qual o horário da loja da minha cidade?", "O horário de funcionamento inclui os feriados municipais?",
            "Qual o horário de verão de vocês?", "A loja abre mais cedo durante a semana?",
            "Qual o horário limite para entrar na loja?", "O horário do drive-thru é diferente?",
            "Poderia me informar o horário de atendimento, por gentileza?",
            "A que horas vocês encerram as atividades hoje?", "Qual o horário de expediente?",
            "Vocês abrem todos os dias da semana?", "Qual o horário de funcionamento da loja online?",
            "O horário de atendimento é contínuo?", "Qual o horário de funcionamento aos sábados e domingos?",
        ]
    },
    "oos": {
        "examples": [
            "Qual a previsão do tempo para amanhã?", "Me conta uma piada engraçada", "Quem vai ganhar o jogo hoje?",
            "Qual o sentido da vida?", "Você tem sentimentos?", "Qual a capital do Japão?",
            "Me passa uma receita de bolo de fubá", "Traduza 'bom dia' para espanhol",
            "Quem escreveu Dom Casmurro?", "Qual o seu nome?", "Você é um robô ou uma pessoa?",
            "Vamos falar sobre filosofia", "Recomende um filme de comédia", "Qual o preço da gasolina hoje?",
            "Como está o trânsito na minha cidade?", "Quero pedir uma pizza de calabresa", "Chame um carro pra mim",
            "Qual o resultado da mega-sena?", "Qual a cotação do euro?", "Você pode cantar uma música?",
            "Qual sua cor favorita?", "Quem te programou?", "O que você acha sobre inteligência artificial?",
            "Existem extraterrestres?", "Como eu faço para ganhar na loteria?", "asdfghjklç",
            "123456", "bla bla bla wiskas sache", "isso é um teste do sistema",
            "Qual a raiz quadrada de 81?", "Quem descobriu o Brasil?", "O que é um buraco negro?",
            "Qual a distância da Terra até a Lua?", "Você sonha?", "Qual a sua idade?",
            "Cante a música do pintinho amarelinho", "Qual o melhor time de futebol do mundo?",
            "Como fazer um avião de papel?", "Você gosta de mim?", "Qual o seu signo?",
            "Existe vida em outros planetas?", "Qual a população da China?", "Onde você mora?",
            "Você pode me dar dinheiro?", "Qual o seu propósito?", "Quem é o presidente do Brasil?",
            "Como consertar uma torneira pingando?", "Me dê um conselho amoroso.",
            "Qual a melhor maneira de aprender inglês?", "Você pode me contar um segredo?",
            "Qual a fórmula de Bhaskara?", "Quem foi Albert Einstein?", "Você pode sentir dor?",
            "Qual o significado do seu nome?", "Recomende um livro de suspense.", "Como fazer café?",
            "Você fica cansado?", "Qual a sua comida favorita?", "Você acredita em Deus?",
            "Qual a sua opinião sobre política?", "O que você faz no seu tempo livre?",
            "Você tem irmãos?", "Qual a sua música preferida?", "Quem ganha numa luta entre um leão e um tigre?",
            "Por que o céu é azul?", "Como a internet funciona?", "Você pode aprender coisas novas sozinho?",
            "Qual foi o seu dia mais feliz?", "Você tem medo de alguma coisa?", "Qual o animal mais rápido do mundo?",
            "Como se joga xadrez?", "Você pode me ajudar com meu dever de casa de matemática?",
            "Qual a montanha mais alta do mundo?", "Você pode criar uma imagem para mim?",
            "O que acontece depois da morte?", "Você pode me ligar?", "Qual o seu filme favorito?",
            "Você pode fazer uma reserva em um restaurante para mim?", "Quem vai ganhar as eleições?",
            "Você pode me contar uma história de ninar?", "Qual o seu maior sonho?",
            "Como eu posso ser feliz?", "Você pode me dar um abraço?", "Qual a senha do Wi-Fi?",
            "Você pode me emprestar seu carro?", "O que é o amor?", "Você pode fazer meu trabalho por mim?",
            "Qual o seu YouTuber favorito?", "Você pode me dar um feedback sobre a minha aparência?",
            "Qual o melhor lugar para viajar nas férias?", "Você pode me contar o final do filme que estou assistindo?",
            "xyz", "quero um poema", "história da arte", "fale sobre carros", "qual o seu hobby?",
        ]
    },
    "buscar_produto_por_categoria": {
        "examples": [
            "Gostaria de ver as [televisões](categoria_produto) que vocês têm.",
            "Estou procurando por [smartphones](categoria_produto).",
            "Quais são as opções na categoria de [notebooks](categoria_produto)?",
            "Mostre-me os [consoles de videogame](categoria_produto).",
            "Quero ver os [fones de ouvido](categoria_produto).",
            "Poderia me mostrar os [tablets](categoria_produto)?",
            "Estou interessado em [smartwatches](categoria_produto).",
            "Quais [geladeiras](categoria_produto) vocês têm disponíveis?",
            "Me mostra a seção de [fogões](categoria_produto).",
            "Preciso de [máquinas de lavar](categoria_produto).",
            "Quais são os modelos de [ar-condicionado](categoria_produto)?",
            "Gostaria de ver a categoria de [câmeras fotográficas](categoria_produto).",
            "Tem [drones](categoria_produto) para vender?",
            "Quero dar uma olhada nos [monitores](categoria_produto).",
            "Me mostre as opções de [impressoras](categoria_produto).",
            "Estou buscando na seção de [eletroportáteis](categoria_produto).",
            "Quais [liquidificadores](categoria_produto) vocês oferecem?",
            "Mostre-me as [batedeiras](categoria_produto).",
            "Preciso de um [micro-ondas](categoria_produto).",
            "Gostaria de ver os [aspiradores de pó](categoria_produto).",
            "Quais são as [caixas de som](categoria_produto) disponíveis?",
            "Estou procurando por [home theaters](categoria_produto).",
            "Me mostre a linha de [produtos de beleza](categoria_produto).",
            "Quero ver os [perfumes](categoria_produto).",
            "Quais [videogames](categoria_produto) vocês têm?",
            "Mostre-me os [celulares](categoria_produto).",
            "Na seção de [computadores](categoria_produto), o que vocês têm?",
            "Gostaria de ver os [laptops](categoria_produto).",
            "Me mostre os [aparelhos de som](categoria_produto).",
            "Quais as opções de [wearables](categoria_produto)?",
            "Estou de olho nos [eletrodomésticos](categoria_produto).",
            "Me mostre a categoria [linha branca](categoria_produto).",
            "Quero ver as [ferramentas elétricas](categoria_produto).",
            "Mostre-me os [artigos esportivos](categoria_produto).",
            "Quais [bicicletas](categoria_produto) vocês vendem?",
            "Estou procurando [brinquedos](categoria_produto).",
            "Me mostre a seção de [livros](categoria_produto).",
            "Gostaria de ver as opções de [móveis](categoria_produto).",
            "Quais [sofás](categoria_produto) estão disponíveis?",
            "Preciso de uma [cama](categoria_produto) nova.",
            "Mostre-me a categoria de [utilidades domésticas](categoria_produto).",
            "Quero ver os [artigos de decoração](categoria_produto).",
            "Quais são as [panelas](categoria_produto) que vocês têm?",
            "Estou interessado na categoria de [áudio e vídeo](categoria_produto).",
            "Me mostre os [equipamentos de informática](categoria_produto).",
            "Gostaria de ver os [acessórios para celular](categoria_produto).",
            "Quais [capinhas](categoria_produto) vocês têm?",
            "Mostre-me os [carregadores](categoria_produto).",
            "Preciso de [mouses](categoria_produto).",
            "Quero ver os [teclados](categoria_produto).",
            "Quais [webcams](categoria_produto) vocês oferecem?",
            "Me mostre os [roteadores](categoria_produto).",
            "Estou procurando por [cadeiras gamer](categoria_produto).",
            "Mostre-me a seção de [games](categoria_produto).",
            "Quais [jogos de ps5](categoria_produto) vocês têm?",
            "Gostaria de ver os [controles de videogame](categoria_produto).",
            "Me mostre a categoria de [instrumentos musicais](categoria_produto).",
            "Quero ver os [violões](categoria_produto).",
            "Quais [guitarras](categoria_produto) vocês têm?",
            "Mostre-me os [teclados musicais](categoria_produto).",
            "Estou interessado em [baterias eletrônicas](categoria_produto).",
            "Me mostre a seção de [saúde e bem-estar](categoria_produto).",
            "Quais [massageadores](categoria_produto) vocês têm?",
            "Gostaria de ver os [monitores de pressão arterial](categoria_produto).",
            "Mostre-me as [balanças digitais](categoria_produto).",
            "Quero ver a categoria de [bebês](categoria_produto).",
            "Quais [carrinhos de bebê](categoria_produto) vocês vendem?",
            "Estou procurando por [berços](categoria_produto).",
            "Me mostre a seção de [pet shop](categoria_produto).",
            "Quais [rações para cachorro](categoria_produto) vocês têm?",
            "Gostaria de ver os [brinquedos para gato](categoria_produto).",
            "Mostre-me a categoria de [automotivo](categoria_produto).",
            "Quero ver os [pneus](categoria_produto).",
            "Quais [centrais multimídia](categoria_produto) vocês têm?",
            "Estou interessado em [ferramentas manuais](categoria_produto).",
            "Me mostre a seção de [jardinagem](categoria_produto).",
            "Quais [cortadores de grama](categoria_produto) vocês vendem?",
            "Gostaria de ver a categoria de [papelaria](categoria_produto).",
            "Mostre-me os [cadernos](categoria_produto).",
            "Quero ver as [canetas](categoria_produto).",
            "Estou procurando por [mochilas](categoria_produto).",
            "Me mostre a seção de [malas de viagem](categoria_produto).",
            "Quais [relógios](categoria_produto) vocês têm?",
            "Gostaria de ver os [óculos de sol](categoria_produto).",
            "Mostre-me a categoria de [moda](categoria_produto).",
            "Quero ver as [camisetas](categoria_produto).",
            "Quais [calças jeans](categoria_produto) vocês têm?",
            "Estou interessado em [tênis](categoria_produto).",
            "Me mostre a seção de [calçados](categoria_produto).",
            "Gostaria de ver os [sapatos sociais](categoria_produto).",
            "Mostre-me as [sandálias](categoria_produto).",
            "Quero ver a categoria de [beleza e perfumaria](categoria_produto).",
            "Quais [maquiagens](categoria_produto) vocês têm?",
            "Mostre-me os [cremes hidratantes](categoria_produto)."
        ]
    },
    "informar_produto_e_categoria": {
        "examples": [
            "Quero ver o [iPhone 17 Pro](produto_especifico) na seção de [smartphones](categoria_produto).",
            "Busco o [MacBook Air M4](produto_especifico), que é um [notebook](categoria_produto).",
            "Me mostre os [fones de ouvido](categoria_produto) do modelo [Sony WH-1000XM6](produto_especifico).",
            "Estou procurando o [Galaxy S25 Ultra](produto_especifico), da categoria de [smartphones](categoria_produto).",
            "Na categoria de [consoles de videogame](categoria_produto), eu quero o [PlayStation 5 Slim](produto_especifico).",
            "Gostaria de informações sobre o [Dell XPS 15](produto_especifico), que é um [notebook](categoria_produto).",
            "Vocês têm o [Nintendo Switch OLED](produto_especifico) na seção de [consoles de videogame](categoria_produto)?",
            "Busco pelo [Pixel 10](produto_especifico) na categoria de [smartphones](categoria_produto).",
            "Quero o [Xbox Series X](produto_especifico), que fica na seção de [consoles de videogame](categoria_produto).",
            "O [HP Spectre x360](produto_especifico) da categoria de [notebooks](categoria_produto), por favor.",
            "Me interessei pelo [Sony WH-1000XM6](produto_especifico), que é um tipo de [fone de ouvido](categoria_produto).",
            "Estou buscando o [iPhone 17 Pro](produto_especifico), um item da categoria [smartphones](categoria_produto).",
            "Na categoria de [notebooks](categoria_produto), vocês têm o [MacBook Air M4](produto_especifico)?",
            "Gostaria de ver o [PlayStation 5 Slim](produto_especifico), que é um [console de videogame](categoria_produto).",
            "Procuro pelo [Galaxy S25 Ultra](produto_especifico) na área de [smartphones](categoria_produto).",
            "O [Dell XPS 15](produto_especifico) é um [notebook](categoria_produto), correto? Quero vê-lo.",
            "Me mostre o [Nintendo Switch OLED](produto_especifico), que se enquadra em [consoles de videogame](categoria_produto).",
            "O produto é o [Pixel 10](produto_especifico) e a categoria é [smartphones](categoria_produto).",
            "Na seção de [consoles de videogame](categoria_produto), estou procurando o [Xbox Series X](produto_especifico).",
            "Gostaria de saber mais sobre o [HP Spectre x360](produto_especifico), um [notebook](categoria_produto) que vocês vendem.",
            "Busco especificamente pelos [fones de ouvido](categoria_produto) modelo [Sony WH-1000XM6](produto_especifico).",
            "Quero o [iPhone 17 Pro](produto_especifico). Ele está na categoria [smartphones](categoria_produto), certo?",
            "O [MacBook Air M4](produto_especifico) é um [notebook](categoria_produto). Me mostre as opções.",
            "Mostre-me o [PlayStation 5 Slim](produto_especifico) da categoria de [consoles de videogame](categoria_produto).",
            "Estou atrás do [Galaxy S25 Ultra](produto_especifico), que é um [smartphone](categoria_produto).",
            "O [Dell XPS 15](produto_especifico) (um [notebook](categoria_produto)) está disponível?",
            "Na categoria [consoles de videogame](categoria_produto), quero informações do [Nintendo Switch OLED](produto_especifico).",
            "O [Pixel 10](produto_especifico) da categoria [smartphones](categoria_produto) está em estoque?",
            "Quero o [Xbox Series X](produto_especifico). A categoria é [consoles de videogame](categoria_produto).",
            "O [HP Spectre x360](produto_especifico), que é da categoria de [notebooks](categoria_produto), me interessa.",
            "Dos [fones de ouvido](categoria_produto), eu quero o [Sony WH-1000XM6](produto_especifico).",
            "Quero o [smartphone](categoria_produto) [iPhone 17 Pro](produto_especifico).",
            "Busco pelo [notebook](categoria_produto) [MacBook Air M4](produto_especifico).",
            "Quero o [console de videogame](categoria_produto) [PlayStation 5 Slim](produto_especifico).",
            "Estou procurando o [smartphone](categoria_produto) [Galaxy S25 Ultra](produto_especifico).",
            "Gostaria de ver o [notebook](categoria_produto) [Dell XPS 15](produto_especifico).",
            "Mostre-me o [console de videogame](categoria_produto) [Nintendo Switch OLED](produto_especifico).",
            "O [smartphone](categoria_produto) que eu quero é o [Pixel 10](produto_especifico).",
            "Na categoria [consoles de videogame](categoria_produto), busco o [Xbox Series X](produto_especifico).",
            "O [notebook](categoria_produto) que me interessa é o [HP Spectre x360](produto_especifico).",
            "O [fone de ouvido](categoria_produto) que procuro é o [Sony WH-1000XM6](produto_especifico).",
            "Sobre [smartphones](categoria_produto), quero saber do [iPhone 17 Pro](produto_especifico).",
            "De [notebooks](categoria_produto), me mostre o [MacBook Air M4](produto_especifico).",
            "Em [consoles de videogame](categoria_produto), me fale sobre o [PlayStation 5 Slim](produto_especifico).",
            "Sobre [smartphones](categoria_produto), o que me dizem do [Galaxy S25 Ultra](produto_especifico)?",
            "Da categoria [notebooks](categoria_produto), me interessei pelo [Dell XPS 15](produto_especifico).",
            "Em [consoles de videogame](categoria_produto), tem o [Nintendo Switch OLED](produto_especifico)?",
            "Quero saber sobre o [Pixel 10](produto_especifico), que é um [smartphone](categoria_produto).",
            "O [Xbox Series X](produto_especifico) é um [console de videogame](categoria_produto), certo? Quero ver.",
            "Gostaria de informações do [HP Spectre x360](produto_especifico) na seção de [notebooks](categoria_produto).",
            "O [Sony WH-1000XM6](produto_especifico), que é um [fone de ouvido](categoria_produto), está à venda?",
            "Estou procurando um [smartphone](categoria_produto), mais especificamente o [iPhone 17 Pro](produto_especifico).",
            "Busco um [notebook](categoria_produto), o modelo [MacBook Air M4](produto_especifico).",
            "Quero um [console de videogame](categoria_produto), o [PlayStation 5 Slim](produto_especifico).",
            "Procuro por um [smartphone](categoria_produto), o [Galaxy S25 Ultra](produto_especifico).",
            "Gostaria de um [notebook](categoria_produto), o [Dell XPS 15](produto_especifico).",
            "Quero um [console de videogame](categoria_produto), o [Nintendo Switch OLED](produto_especifico).",
            "Busco um [smartphone](categoria_produto), o [Pixel 10](produto_especifico).",
            "Estou interessado em um [console de videogame](categoria_produto), o [Xbox Series X](produto_especifico).",
            "Procuro por um [notebook](categoria_produto), o [HP Spectre x360](produto_especifico).",
            "Gostaria de um [fone de ouvido](categoria_produto), o modelo [Sony WH-1000XM6](produto_especifico).",
            "O produto que eu quero é o [iPhone 17 Pro](produto_especifico) da categoria [smartphones](categoria_produto).",
            "Me mostre o [MacBook Air M4](produto_especifico) da seção de [notebooks](produto_especifico).",
            "Quero ver o [PlayStation 5 Slim](produto_especifico) que é da categoria [consoles de videogame](categoria_produto).",
            "O [Galaxy S25 Ultra](produto_especifico) (categoria: [smartphones](categoria_produto)), por favor.",
            "Busco o [Dell XPS 15](produto_especifico) ([notebook](categoria_produto)).",
            "O [Nintendo Switch OLED](produto_especifico) da categoria [consoles de videogame](categoria_produto), por gentileza.",
            "Me informe sobre o [Pixel 10](produto_especifico), que é um [smartphone](categoria_produto).",
            "O [Xbox Series X](produto_especifico), um [console de videogame](categoria_produto), está disponível?",
            "Quero o [HP Spectre x360](produto_especifico) da linha de [notebooks](categoria_produto).",
            "O [Sony WH-1000XM6](produto_especifico) da categoria [fones de ouvido](categoria_produto), tem?",
            "Quero ver o [smartphone](categoria_produto) chamado [iPhone 17 Pro](produto_especifico).",
            "Me mostre o [notebook](categoria_produto) de modelo [MacBook Air M4](produto_especifico).",
            "Estou interessado no [console de videogame](categoria_produto) [PlayStation 5 Slim](produto_especifico).",
            "O [smartphone](categoria_produto) que eu busco é o [Galaxy S25 Ultra](produto_especifico).",
            "Gostaria de ver o [notebook](categoria_produto) de nome [Dell XPS 15](produto_especifico).",
            "Me mostre o [console de videogame](categoria_produto) específico [Nintendo Switch OLED](produto_especifico).",
            "O [smartphone](categoria_produto) em questão é o [Pixel 10](produto_especifico).",
            "Busco o [console de videogame](categoria_produto) [Xbox Series X](produto_especifico).",
            "O [notebook](categoria_produto) que eu quero ver é o [HP Spectre x360](produto_especifico).",
            "Quero os [fones de ouvido](categoria_produto) de modelo [Sony WH-1000XM6](produto_especifico)."
        ]
    },
    "perguntar_preco": {
        "examples": [
            "Quanto custa o [iPhone 17 Pro](produto_especifico)?",
            "Por quanto sai o [MacBook Air M4](produto_especifico)?",
            "Qual o preço do [Galaxy S25 Ultra](produto_especifico)?",
            "Me diga o valor do [PlayStation 5 Slim](produto_especifico).",
            "Quanto é o [Xbox Series X](produto_especifico)?",
            "Qual o preço do [Nintendo Switch OLED](produto_especifico)?",
            "Gostaria de saber o preço do [Dell XPS 15](produto_especifico).",
            "Por quanto está o [HP Spectre x360](produto_especifico)?",
            "Qual o valor do [Sony WH-1000XM6](produto_especifico)?",
            "Quanto eu pago pelo [Pixel 10](produto_especifico)?",
            "Preço do [iPhone 17 Pro](produto_especifico), por favor.",
            "Valor do [MacBook Air M4](produto_especifico)?",
            "O [Galaxy S25 Ultra](produto_especifico) custa quanto?",
            "O [PlayStation 5 Slim](produto_especifico) está por quanto?",
            "Qual o preço do [Xbox Series X](produto_especifico) hoje?",
            "Me informa o valor do [Nintendo Switch OLED](produto_especifico).",
            "Quanto custa em reais o [Dell XPS 15](produto_especifico)?",
            "O [HP Spectre x360](produto_especifico) sai a quanto?",
            "Poderia me dizer o preço do [Sony WH-1000XM6](produto_especifico)?",
            "Qual o custo do [Pixel 10](produto_especifico)?",
            "Estou interessado no preço do [iPhone 17 Pro](produto_especifico).",
            "Qual é a facada pelo [MacBook Air M4](produto_especifico)?",
            "Me vê o preço do [Galaxy S25 Ultra](produto_especifico).",
            "Quanto está custando o [PlayStation 5 Slim](produto_especifico)?",
            "O [Xbox Series X](produto_especifico), qual o valor?",
            "Gostaria de saber o valor do [Nintendo Switch OLED](produto_especifico).",
            "Qual o preço de tabela do [Dell XPS 15](produto_especifico)?",
            "Por qual valor consigo comprar o [HP Spectre x360](produto_especifico)?",
            "Qual o preço final do [Sony WH-1000XM6](produto_especifico)?",
            "Quanto de dinheiro eu preciso para ter um [Pixel 10](produto_especifico)?",
            "Valor, por favor, do [iPhone 17 Pro](produto_especifico).",
            "Preço do [MacBook Air M4](produto_especifico)?",
            "E o [Galaxy S25 Ultra](produto_especifico), quanto custa?",
            "Diga-me o preço do [PlayStation 5 Slim](produto_especifico).",
            "O [Xbox Series X](produto_especifico) está saindo por quanto?",
            "Quanto custa o [Nintendo Switch OLED](produto_especifico) à vista?",
            "Qual o preço parcelado do [Dell XPS 15](produto_especifico)?",
            "O [HP Spectre x360](produto_especifico) tem desconto? Qual o preço?",
            "Qual o valor de mercado do [Sony WH-1000XM6](produto_especifico)?",
            "O [Pixel 10](produto_especifico), qual o preço de lançamento?",
            "Qual o preço do [iPhone 17 Pro](produto_especifico) de 256GB?",
            "O [MacBook Air M4](produto_especifico) com 16GB de RAM custa quanto?",
            "Me passe o orçamento para o [Galaxy S25 Ultra](produto_especifico).",
            "O [PlayStation 5 Slim](produto_especifico) com um jogo, qual o valor?",
            "Quanto sai o [Xbox Series X](produto_especifico) com dois controles?",
            "Preço do bundle do [Nintendo Switch OLED](produto_especifico) com Mario Kart?",
            "Qual o valor do [Dell XPS 15](produto_especifico) com a melhor configuração?",
            "O [HP Spectre x360](produto_especifico) na cor azul, qual o preço?",
            "Gostaria de uma cotação para o [Sony WH-1000XM6](produto_especifico).",
            "O [Pixel 10](produto_especifico) branco custa quanto?",
            "Qual o valor do [iPhone 17 Pro](produto_especifico) no boleto?",
            "Por quanto eu levo o [MacBook Air M4](produto_especifico) hoje?",
            "O [Galaxy S25 Ultra](produto_especifico) tem alguma promoção? Qual o preço?",
            "Qual o valor do [PlayStation 5 Slim](produto_especifico) usado?",
            "O [Xbox Series X](produto_especifico) seminovo, quanto custa?",
            "Qual o preço do [Nintendo Switch OLED](produto_especifico) desbloqueado?",
            "O [Dell XPS 15](produto_especifico) da geração passada, qual o valor?",
            "Quanto custa o [HP Spectre x360](produto_especifico) de vitrine?",
            "Qual o valor do [Sony WH-1000XM6](produto_especifico) reembalado?",
            "O [Pixel 10](produto_especifico) importado sai por quanto?",
            "Me diga o preço do [iPhone 17 Pro](produto_especifico), por gentileza.",
            "O [MacBook Air M4](produto_especifico), qual o valor final?",
            "Quanto preciso desembolsar pelo [Galaxy S25 Ultra](produto_especifico)?",
            "O [PlayStation 5 Slim](produto_especifico) está em que faixa de preço?",
            "Qual o custo de aquisição do [Xbox Series X](produto_especifico)?",
            "O [Nintendo Switch OLED](produto_especifico) vale quanto?",
            "Poderia informar o preço do [Dell XPS 15](produto_especifico)?",
            "O [HP Spectre x360](produto_especifico) está quanto?",
            "Gostaria de saber o preço do [Sony WH-1000XM6](produto_especifico) agora.",
            "Qual o preço atual do [Pixel 10](produto_especifico)?",
            "O [iPhone 17 Pro](produto_especifico), me fale sobre o preço.",
            "O [MacBook Air M4](produto_especifico), e o preço?",
            "Quero saber o preço do [Galaxy S25 Ultra](produto_especifico).",
            "Preço do [PlayStation 5 Slim](produto_especifico).",
            "Valor do [Xbox Series X](produto_especifico).",
            "Preço do [Nintendo Switch OLED](produto_especifico).",
            "Preço do [Dell XPS 15](produto_especifico).",
            "Valor do [HP Spectre x360](produto_especifico).",
            "Preço do [Sony WH-1000XM6](produto_especifico).",
            "Valor do [Pixel 10](produto_especifico)."
        ]
    }
}


MAPA_PRODUTO_CATEGORIA = {
    "iphone 17 pro": "smartphones",
    "galaxy s25 ultra": "smartphones",
    "pixel 10": "smartphones",
    "playstation 5 slim": "consoles de videogame",
    "xbox series x": "consoles de videogame",
    "nintendo switch oled": "consoles de videogame",
    "macbook air m4": "notebooks",
    "dell xps 15": "notebooks",
    "hp spectre x360": "notebooks",
    "sony wh-1000xm6": "fones de ouvido"
}

# ===================================================================================
# 2. LÓGICA DE TRANSFORMAÇÃO (COM ENRIQUECIMENTO DE METADADOS)
# ===================================================================================

def transformar_dataset(dados_brutos):
    dataset_estruturado = []
    pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

    for intent, data in dados_brutos.items():
        for frase_com_anotacao in data.get('examples', []):
            entidades_finais = []
            texto_limpo = ""
            ultimo_idx = 0
            
            # 1. Extrai todas as entidades explícitas do texto
            for match in pattern.finditer(frase_com_anotacao):
                inicio_match, fim_match = match.span()
                valor_entidade = match.group(1)
                tipo_entidade = match.group(2)

                texto_limpo += frase_com_anotacao[ultimo_idx:inicio_match]
                
                inicio_entidade = len(texto_limpo)
                texto_limpo += valor_entidade
                fim_entidade = len(texto_limpo)
                
                entidades_finais.append({
                    "entity": tipo_entidade,
                    "value": valor_entidade,
                    "start": inicio_entidade,
                    "end": fim_entidade,
                    "source": ["text"]  # Adiciona a origem inicial como 'text'
                })
                
                ultimo_idx = fim_match

            texto_limpo += frase_com_anotacao[ultimo_idx:]
            
            # 2. Lógica de Validação e Enriquecimento
            produto_encontrado = None
            for ent in entidades_finais:
                if ent['entity'] == 'produto_especifico':
                    produto_encontrado = ent
                    break
            
            # Se um produto foi encontrado, tenta validar/inferir a categoria
            if produto_encontrado:
                nome_produto = produto_encontrado['value'].lower()
                categoria_inferida = MAPA_PRODUTO_CATEGORIA.get(nome_produto)

                if categoria_inferida:
                    categoria_explícita_encontrada = False
                    # Procura por uma categoria explícita correspondente para enriquecer
                    for ent in entidades_finais:
                        if ent['entity'] == 'categoria_produto' and ent['value'].lower() in categoria_inferida:
                            # ENRIQUECE: A categoria explícita foi confirmada pela inferência
                            ent['source'].append('inference')
                            print(f"INFO [Enriquecimento]: Entidade '{ent['value']}' na frase '{texto_limpo}' foi validada por inferência.")
                            categoria_explícita_encontrada = True
                            break
                    
                    # INFERE: Se nenhuma categoria explícita foi encontrada, adiciona uma nova
                    if not categoria_explícita_encontrada:
                        entidades_finais.append({
                            "entity": "categoria_produto",
                            "value": categoria_inferida,
                            "source": ["inference"] # A origem é apenas por inferência
                        })
                        print(f"INFO [Inferência]: Nova entidade '{categoria_inferida}' inferida na frase '{texto_limpo}'.")


            dataset_estruturado.append({
                "text": texto_limpo,
                "intent": intent,
                "entities": entidades_finais
            })

    return dataset_estruturado

# ===================================================================================
# 3. SCRIPT PRINCIPAL (Sem alterações)
# ===================================================================================

def main():
    """
    Função principal que orquestra a transformação e o salvamento do arquivo.
    """
    print("Iniciando a transformação do dataset...")

    dados_finais_nlu = transformar_dataset(nlu_dataset_bruto)
    
    diretorio_output = "datasets"
    os.makedirs(diretorio_output, exist_ok=True)
    
    nome_arquivo = "loja_eletronico_corrigido.json"
    caminho_arquivo_saida = os.path.join(diretorio_output, nome_arquivo)

    try:
        with open(caminho_arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(dados_finais_nlu, f, ensure_ascii=False, indent=4)
        print(f"\nDataset transformado com sucesso!")
        print(f"Total de {len(dados_finais_nlu)} exemplos de treinamento gerados.")
        print(f"Arquivo salvo em: {caminho_arquivo_saida}")
    except Exception as e:
        print(f"\nOcorreu um erro ao salvar o arquivo: {e}")


if __name__ == "__main__":
    main()