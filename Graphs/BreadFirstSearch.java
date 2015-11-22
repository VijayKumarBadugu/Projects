import java.io.*;
import java.util.*;
public class BreadFirstSearch {
	int V;
	LinkedList<Integer> adjacency[];
	BreadFirstSearch(int v)
	{
		V	=	v;
		adjacency	=	new LinkedList[v];
		int i;
		for(i=0;i<V;i++)
		{
			adjacency[i]	=	new LinkedList();
		}
	}
	void Add_Edge(int u,int v)
	{
		adjacency[u].add(v);
	}
	
	void BFS(int s)
	{
		boolean visited[]	=	new boolean[V];
		for(int j=0;j<V;j++)
		{
			visited[j]	=	false;
		}
		
		LinkedList<Integer> queue	= new LinkedList<Integer>();
		queue.add(s);
		while(queue.size()!=0)
		{
			int variable	=	queue.removeFirst();
			System.out.println(variable);
			visited[variable] = true;
			Iterator<Integer> i = adjacency[variable].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
		}
	}
	
	public static void main(String args[]) {
		BreadFirstSearch g = new BreadFirstSearch(4);
		 
        g.Add_Edge(0, 1);
        g.Add_Edge(0, 2);
        g.Add_Edge(1, 2);
        g.Add_Edge(2, 0);
        g.Add_Edge(2, 3);
        g.Add_Edge(3, 3);
 
        System.out.println("Following is Breadth First Traversal "+
                           "(starting from vertex 2)");
 
        g.BFS(2);
		
	}
}
