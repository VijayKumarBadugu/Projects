import java.io.*;
import java.util.*;
public class CycleDetection {
	int V;
	LinkedList<Integer> adjacency[];
	CycleDetection(int v)
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
	
	boolean DepthFirst(int u, boolean visited[],boolean stack[])
	{
		Iterator<Integer> i = adjacency[u].listIterator();
		visited[u]	=	true;
		stack[u]	=	true;
		
		while(i.hasNext())
		{
			int v	=	i.next();
			if(visited[v]==false)
			{
				if(DepthFirst(v,visited,stack)==true)
				{
					return true;
				}
			}
			else
			{
				if(stack[v]==true)
				{
					return true;
				}
			}
			
			
		}
		stack[u]	=	false;
		return false;
	}
	boolean isCycle()
	{
		boolean visited[]	= 	new boolean[V];
		boolean stack[]		=	new boolean[V];
		for(int i=0;i<V;i++)
		{
			visited[i]	=	false;
		}
		for(int i=0;i<V;i++)
		{
			stack[i]	=	false;
		}
		
		for(int i=0;i<V;i++)
		{
			if(DepthFirst(i,visited,stack)==true)
			{
				return true;
			}
		}
		return false;
	}
	public static void main(String args[])
    {
		CycleDetection g = new CycleDetection(4);
 
		g.addEdge(0, 1);
	    g.addEdge(0, 2);
	    g.addEdge(2,2);
	    
 
	    System.out.print(g.isCycle());
 
       
    }

}
