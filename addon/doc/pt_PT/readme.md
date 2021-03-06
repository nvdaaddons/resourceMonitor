# Monitor de Recursos #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Baixar [versão estável][1]
* NVDA compatibility: 2017.4 to 2019.3

Este extra fornece informações sobre carga da CPU, uso de memória e outras
informações de uso de recursos.

# Teclas de atalho: #

* NVDA+Shift+E apresenta A memória ram usada, a carga média do processador e
  as informações da bateria, se disponíveis.
* NVDA + Shift + 1 Apresenta a carga média do processador e se existirem
  vários processadores, fornece a carga de cada núcleo.
* NVDA+Shift+2/5 Apresenta o espaço usado e total para a memória ram física
  e virtual.
* NVDA+Shift+3 Apresenta o espaço usado e total das unidades estáticas e
  removíveis.
* NVDA+Shift+4 Apresenta a percentagem da bateria, o estado da carga, o
  tempo restante (se não estiver a carregar) e um aviso se a bateria estiver
  fraca ou crítica.
* NVDA+Shift+6 apresenta a arquitectura da CPU 32/64 bits e a versão do
  Windows e os números do service pack.
* NVDA+Shift+7 apresenta o tempo de actividade do sistema.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## Notas de utilização: ##

Este extra não substitui o gestor de tarefas e outros programas de
informações do sistema para o Windows. Observe também o seguinte:

* O uso da CPU é dado para processadores lógicos, e não para núcleos
  físicos. Isso é notável para os processadores que usam o Hyper-Threading,
  onde o número de CPU é o dobro do número de núcleos da CPU.
* Se houver uma grande actividade do disco, como copiar ficheiros grandes,
  pode haver atrasos ao obter informações de uso do disco.
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Versão 18.04

A versão 18.04.x é a última versão a suportar versões anteriores ao Windows
7 SP1.

* Última versão para suporte ao Windows Server 2003, Vista e Server 2008.
* Melhor detecção de versões do Windows 10 e distinção entre versões
  públicas e beta privadas.

## Versão 17.12

* Adicionado suporte para processadores ARM de 64 bits no Windows 10.

## Versão 17.09

Importante: a versão 17.09.x é a última versão a suportar o Windows XP.

* Última versão para executar no Windows XP.
* O Windows 10 build 16278 e posterior é reconhecido como a Versão 1709. Uma
  revisão menor para este extra será lançada logo que a versão estável da
  versão 1709 seja lançada.

## Versão 17.07.1

* Reintroduz o suporte para o Windows XP (quebrado desde a versão 17.02).

## Versão 17.05

* Anúncio do tempo de actividade do sistema (tempo passado desde a última
  inicialização, NVDA + Shift + 7).

## Versão 17.02

* Dependência psutil actualizada para 5.0.1.
* Ao verificar o uso do disco, o NVDA deixará de apresentar uma caixa de
  diálogo de erro em alguns sistemas onde uma mídia removível não está
  devidamente reconhecida (como, por exemplo, quando um cartão não está
  inserido em um leitor de cartão).

## Versão 16.08

A partir da versão 16.08, os lançamentos adicionais serão mostrados como
ano.mês.revisão.

* Várias revisões do Windows 10 agora são devidamente reconhecidas (como a
  1607 para a compilação 14393).
* As revisões de compilação do Windows 10 (após a instalação de
  actualizações cumulativas) são devidamente reconhecidas (como a 14393.51).
* Se estiver usando versões de Insider Preview, esse fato é reconhecido.

## Mudanças para 4.5 ##

* O repositório do extra foi movido para o GitHub (pode ser encontrado em
  https://github.com/josephsl/resourcemonitor).
* O Windows Server 2016 é devidamente reconhecido.

## Alterações para 4.0 ##

* Dependência psutil actualizada para 2.2.1.
* Melhorado o desempenho na rapidez ao obter informações sobre a carga da
  CPU.
* Adicionado suporte para o reconhecimento do Windows 10.
* No Windows 10, o número de compilação do Windows também será anunciado.
* Agora, pode usar o gestor de extras para obter ajuda.

## Mudanças para 3.1 ##

* O monitor de recursos passou a suportar oficialmente o Windows 8.1.
* Traduções actualizadas

## Alterações para 3.0 ##

* Dependência psutil actualizada para 1.2.1.
* Anúncio da versão actual do Windows, arquitetura da CPU e pacote de
  serviço, se houver (NVDA + Shift + 6).
* Possibilidade de alterar as teclas de atalho do add-on (NVDA 2013.3 ou
  posterior).
* Capacidade de copiar informações de recursos individuais para a área de
  transferência ao pressionar os comandos de recursos duas vezes.

## Mudanças para 2.4 ##

* Novos idiomas: chinês (simplificado), ucraniano.
* Traduções actualizadas

## Alterações para 2.3 ##

* Adicionada a tradução búlgara.

## Mudanças para 2.2 ##

* Adicionadas as seguintes traduções: árabe, aragonês, croata, holandês,
  finlandês, francês, galego, alemão, húngaro, italiano, japonês, coreano,
  nepalês, polaco, português (Brasil), russo, eslovaco, esloveno, espanhol,
  tâmil e turco.

## Mudanças para 2.1 ##

* Dependência psutil actualizada para a versão 0.6.1.
* Corrigido grande atraso ao obter informações de unidades.
* Limpeza de códigoCode cleanup.

## Mudanças para 2.0 ##

* Foi adicionado o Suporte de tradução e respectivos comentários.

## Alterações para 1.0 ##

* Lançamento inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
