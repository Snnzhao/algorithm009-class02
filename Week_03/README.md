学习笔记
递归 Recursion
	递归结构： recursion reminator、process logical in current level
	           drill down 、reverse the  current level status if needed
	递归要点：1不要人肉递归 2找最近最简单子方法 3数学归纳法思维
	
	递归模板：
	const recursion = function(level, param1, param2, ...) {
    if (level > MAX_LEVEL) {
         // process result 
         return; 
    }
    // process current logic 
    process(level, param);

  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
  }
	爬楼梯问题：