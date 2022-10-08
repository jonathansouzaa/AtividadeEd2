package ed2;
import java.util.*;

public class Exercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// EX 01
		
		//EX 02
		LinkedList<Integer> carros = new LinkedList<>();
		carros.add(1);
		carros.add(5);
		carros.add(4);
		carros.add(3);
		carros.add(2);
		carros.add(6);
		carros.add(7);
		
		LinkedList<Integer> ordenada = ordenarCarros(carros);
		printzada(ordenada);
		
	}
	
	public static LinkedList<Integer> ordenarCarros(LinkedList<Integer> carros) {
		LinkedList<Integer> ordenada = carros;
		for(int i = 0; i < carros.size() - 1; i++) {
			if(ordenada.get(i) >= ordenada.get(i+1)) {
				int aux = ordenada.get(i);
				ordenada.set(i, ordenada.get(i+1));
				ordenada.set(i+1, aux);
			}
		}
		for(int j = 0; j < carros.size() - 1; j++ ) {
			if(ordenada.get(j) >= ordenada.get(j+1)) {
				ordenada = ordenarCarros(ordenada);
			}
		}
		
		
		return ordenada;
	}
	
	public static void printzada (LinkedList<Integer> lista) {
		Iterator<Integer> itr = lista.iterator();
		
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}
	
}