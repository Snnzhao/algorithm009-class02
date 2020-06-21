学习笔记
递归 Recursion
	递归结构： recursion terminator、process logical in current level
	           drill down 、revert the  current level status if needed
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

分治、回溯的实现和特性
	分治和递归本质上都是找问题的重复性并分解问题
	
	分治代码模板：
		recursion terminator、prepare data、 conquer subproblems、 process and generate the 
		final result
		
		def divide conquer(problem, param1, param2,...)
			#recursion terminator
			if problem is None:
				print_result
				return
			#prepare data
			data=prepare_data(problem)
			subproblems=split_problem(problem, data)
			
			#conquer subproblems
			subresult1=self_divide_conquer(subproblems[0],p1,...)
			subresult2=self_divide_conquer(subproblems[1],p1,...)
			...
			
			#process and generate the final result
			result=process_result(subresult1,subresult2,...)
			
	回溯法：
		
			