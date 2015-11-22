import java.io.*;
import java.util.*;
public class DepthFirstSearch {
	int V;
	LinkedList<Integer> adjacency[];
	DepthFirstSearch(int v)
	{
		V	=	v;
		adjacency	=	new LinkedList[v];
		int i;
		for(i=0;i<V;i++)
		{
			adjacency[i]	=	new LinkedList();
		}
	}
	void addEdge(int u,int v)
	{
		adjacency[u].add(v);
	}
	
	void DepthFirst(int u, boolean visited[])
	{
		Iterator<Integer> i = adjacency[u].listIterator();
		visited[u]	=	true;
		System.out.println(u);
		while(i.hasNext())
		{
			int v	=	i.next();
			if(visited[v]==false)
			{
				DepthFirst(v,visited);
			}
		}
	}
	void DFS(int u)
	{
		boolean visited[]	= new boolean[V];
		for(int i=0;i<V;i++)
		{
			visited[i]	=	false;
		}
		DepthFirst(u,visited);
	}
	
	public static void main(String args[])
    {
		DepthFirstSearch g = new DepthFirstSearch(4);
 
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);
 
        System.out.println("Following is Depth First Traversal "+
                           "(starting from vertex 2)");
 
        g.DFS(2);
    }

}
