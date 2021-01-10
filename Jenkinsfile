node('python') {
  
  def testsDir = "app"
  
  stage("Checkout") {
    git branch: "master", credentialsId: 'git-token-credentials', url: "https://github.com/smeubank/rest-api-scripting"
  } 
	
  stage('REST') {
    dir("${testsDir}"){
	 //uncomment this block of code if u want to execute all test cases
	def result = sh(returnStdout: true, script: "ls *test.py")
        def files = "${result}".split("\n")
        for (file in files) {
          echo("filename : ")
          sh("python ./${file}")
        }
        /*sh("python ./qbP1Orchestrations.py")*/
    }
  }
}
