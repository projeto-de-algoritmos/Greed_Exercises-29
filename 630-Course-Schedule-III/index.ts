function scheduleCourse(cursos: number[][]): number {
  // Ordenar os cursos com base no prazo máximo
  cursos.sort((a, b) => a[1] - b[1]);

  // Tempo acumulado
  let tempo = 0;
  // Contador de cursos realizados
  let quantidade = 0;

  for (const [duracao, prazo] of cursos) {
    // Verificar se é possível realizar o curso dentro do prazo
    if (tempo + duracao <= prazo) {
      // Atualizar o tempo acumulado
      tempo += duracao;
      // Incrementar o contador de cursos realizados
      quantidade++;
    } else {
      let indiceMaximo = -1;
      let prazoMaximo = 0;

      // Encontrar o curso com maior prazo máximo já agendado
      for (let i = 0; i < quantidade; i++) {
        if (cursos[i][1] > prazoMaximo) {
          indiceMaximo = i;
          prazoMaximo = cursos[i][1];
        }
      }

      // Verificar se substituir resulta em menor atraso total
      if (indiceMaximo !== -1 && prazo < prazoMaximo) {
        // Atualizar o tempo acumulado considerando a substituição
        tempo += duracao - cursos[indiceMaximo][0];
        // Substituir o curso de maior prazo máximo pelo curso atual
        cursos[indiceMaximo] = [duracao, prazo];
      }
    }
  }

  return quantidade;
}
