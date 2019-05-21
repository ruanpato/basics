	.file	"2031.cpp"
	.text
	.section	.rodata
.LC0:
	.string	"%d"
.LC1:
	.string	"%s %s"
.LC2:
	.string	"Aniquilacao mutua"
.LC3:
	.string	"Ambos venceram"
.LC4:
	.string	"Sem ganhador"
.LC5:
	.string	"Jogador 1 venceu"
.LC6:
	.string	"Jogador 2 venceu"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	leaq	-24(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	scanf@PLT
.L12:
	movl	-24(%rbp), %eax
	testl	%eax, %eax
	jle	.L2
	leaq	-14(%rbp), %rdx
	leaq	-20(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	scanf@PLT
	movzbl	-18(%rbp), %eax
	cmpb	$97, %al
	jne	.L3
	movzbl	-12(%rbp), %eax
	cmpb	$97, %al
	jne	.L3
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L3:
	movzbl	-18(%rbp), %eax
	cmpb	$112, %al
	jne	.L5
	movzbl	-12(%rbp), %eax
	cmpb	$112, %al
	jne	.L5
	leaq	.LC3(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L5:
	movzbl	-18(%rbp), %eax
	cmpb	$100, %al
	jne	.L6
	movzbl	-12(%rbp), %eax
	cmpb	$100, %al
	jne	.L6
	leaq	.LC4(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L6:
	movzbl	-18(%rbp), %eax
	cmpb	$97, %al
	jne	.L7
	movzbl	-12(%rbp), %eax
	cmpb	$100, %al
	jne	.L7
	leaq	.LC5(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L7:
	movzbl	-12(%rbp), %eax
	cmpb	$97, %al
	jne	.L8
	movzbl	-18(%rbp), %eax
	cmpb	$100, %al
	jne	.L8
	leaq	.LC6(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L8:
	movzbl	-18(%rbp), %eax
	cmpb	$97, %al
	jne	.L9
	movzbl	-12(%rbp), %eax
	cmpb	$112, %al
	jne	.L9
	leaq	.LC5(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L9:
	movzbl	-12(%rbp), %eax
	cmpb	$97, %al
	jne	.L10
	movzbl	-18(%rbp), %eax
	cmpb	$112, %al
	jne	.L10
	leaq	.LC6(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L10:
	movzbl	-18(%rbp), %eax
	cmpb	$100, %al
	jne	.L11
	movzbl	-12(%rbp), %eax
	cmpb	$112, %al
	jne	.L11
	leaq	.LC5(%rip), %rdi
	call	puts@PLT
	jmp	.L4
.L11:
	movzbl	-12(%rbp), %eax
	cmpb	$100, %al
	jne	.L4
	movzbl	-18(%rbp), %eax
	cmpb	$112, %al
	jne	.L4
	leaq	.LC6(%rip), %rdi
	call	puts@PLT
.L4:
	movl	-24(%rbp), %eax
	subl	$1, %eax
	movl	%eax, -24(%rbp)
	jmp	.L12
.L2:
	movl	$0, %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L14
	call	__stack_chk_fail@PLT
.L14:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (GNU) 7.3.1 20180312"
	.section	.note.GNU-stack,"",@progbits
