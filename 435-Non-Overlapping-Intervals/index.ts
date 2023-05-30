function eraseOverlapIntervals(intervalos: number[][]): number {
    // Ordena os intervalos com base no tempo de término
    intervalos.sort((a, b) => a[1] - b[1]); 
    
    // Contador de intervalos a serem removidos
    let contador = 0; 
    // Define o tempo de término do primeiro intervalo
    let fim = intervalos[0][1]; 
    
    for (let i = 1; i < intervalos.length; i++) {
      if (intervalos[i][0] < fim) {
        // Há sobreposição, é necessário remover o intervalo atual
        contador++;
      } else {
        // Não há sobreposição, atualiza o tempo de término
        fim = intervalos[i][1];
      }
    }
  
    return contador;
  }
  