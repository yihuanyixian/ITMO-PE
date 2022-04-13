package Command;

import Collection.Exceptions.ParaIncorrectException;
import Manager.CommandManager;

public class PrintFieldAscendingAnnualTurnover extends AbstractCommand {
    public PrintFieldAscendingAnnualTurnover() {
        this.name = "print_field_ascending_annual_turnover";
        this.description = "Print the values of the annualTurnover field of all elements in ascending order";
    }

    @Override
    public void execute(CommandManager commandManager, String[] para, String saver) {
        if(para.length>1){
            throw new ParaIncorrectException("Error [print_field_ascending_annual_turnover]: This command does not accept any parameter!\n");
        }else {
            commandManager.executePrintFieldAscendingAnnualTurnover();
        }
    }
}
