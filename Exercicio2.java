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
		
		LinkedList<Integer> ordenada = ordernarCarros(carros);
		printzada(ordenada);
		
	}
	
	public static LinkedList<Integer> ordernarCarros(LinkedList<Integer> carros) {
		
		LinkedList<Integer> listaOrdenada = new LinkedList<>();
		listaOrdenada.add(carros.get(0));
		for(int j = 0; j < carros.size(); j++ ) {
			for(int i = listaOrdenada.size(); i < carros.size(); i++) {
				if(carros.get(i) >= listaOrdenada.get(i-1)) {
					listaOrdenada.add(carros.get(i));
				} else {
					int aux = listaOrdenada.get(i-1);
					listaOrdenada.add(i-1, carros.get(i));
				}
			}
		}
		
		return listaOrdenada;
	}
	
	public static void printzada (LinkedList<Integer> lista) {
		Iterator<Integer> itr = lista.iterator();
		
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}
	
}