#include "small_memory_tree/smallMemoryTree.hxx"
#include <iostream>

int main() {
  auto tree = st_tree::tree<int>{};
  tree.insert (0);
  tree.root ().insert (1);
  tree.root ().insert (2);
  auto smt = small_memory_tree::SmallMemoryTree<int>{ tree, 255 };
  auto myChildren = small_memory_tree::childrenByPath (smt, { 0 });
  if( myChildren->size () == 2 && myChildren->at (0) == 1 && myChildren->at (1) == 2){
      std::cout<<"it works"<<std::endl;
    }
  else
    {
      std::terminate();
    }
  return 0;
}
