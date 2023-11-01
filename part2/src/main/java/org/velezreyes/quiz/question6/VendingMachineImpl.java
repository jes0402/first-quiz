package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  public double machineCash = 0;

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }
  
  public void insertQuarter(){
    this.machineCash = this.machineCash + 0.25;
  }

  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException{
    Drink product = null; 

    switch (name) { 
      case "ScottCola":
        product = new ScottCola();
        break;
      case "KarenTea":
        product = new KarenTea();
        break;
      default:
        throw new UnknownDrinkException();
    }
    
    if (product.getPrice() > machineCash) {
      throw new NotEnoughMoneyException();
    }
    return product;
  }
}
