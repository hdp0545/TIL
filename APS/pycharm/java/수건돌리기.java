import java.util.Scanner;
import java.util.ArrayList;

class Main {
  private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame){
    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
		int current = 0;
		int sul = 0;
		ArrayList<Integer> ground = new ArrayList<Integer>();
		ArrayList<Integer> quickers = new ArrayList<Integer>();
		ArrayList<Integer> scores = new ArrayList<Integer>();
		for(int i=0; i<numOfAllPlayers; i++) {
			scores.add(0);
		}
		for(int i=1; i<numOfAllPlayers; i++) {
    	int temp = i;
			ground.add(temp);
		}
		for(int i=0; i<numOfQuickPlayers; i++) {
			int quicker = (int)namesOfQuickPlayers[i] - 65;
			quickers.add(quicker);
		}
		scores.set(0, 1);
		for(int i=0; i<numOfGames; i++) {
			current += numOfMovesPerGame[i];
			if (current < 0) {
				while (current < 0) {
					current += (numOfAllPlayers - 1);
				}
			} else {
				current = current % (numOfAllPlayers - 1);
			}
    	if(quickers.contains(ground.get(current))) {
				scores.set(sul, scores.get(sul) + 1);
			} else {
				int temp = sul;
				sul = ground.get(current);
				ground.set(current, temp);
				scores.set(sul, scores.get(sul) + 1);
			}
		}
		for(int player: ground) {
			char wplayer = (char)(player + 65);
			System.out.print(wplayer);
			System.out.print(' ');
			System.out.println(scores.get(player));
		}
		char wsul = (char)(sul + 65);
		System.out.print(wsul);
		System.out.print(' ');
		System.out.println(scores.get(sul));
  }

  private static class InputData {
    int numOfAllPlayers;
    int numOfQuickPlayers;
    char[] namesOfQuickPlayers;
    int numOfGames;
    int[] numOfMovesPerGame;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

      inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
      System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

      inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.numOfMovesPerGame = new int[inputData.numOfGames];
      String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
      for(int i = 0; i < inputData.numOfGames ; i++){
        inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  }
}